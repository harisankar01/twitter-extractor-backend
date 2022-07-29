from ctypes import pointer
from itertools import count
from dotenv import load_dotenv
from flask import Flask, jsonify, request
import tweepy as tw

load_dotenv()
app = Flask(__name__)

key = "JbYaDTbeBLA1svw8N0rbW9AWc"
key_secret = "8HOFGU54XuVO7JTPjmM6YXLuxweizpdSKs1NQ5MrFWl8KIplki"
access_token = "1438353997765623812-kMMQUS01HTb0XnSOeHKoV1e9g5Uq6I"
access_secret = "bthnVimJ0GLSTTZU9Af5SCYHCClHcnWmJDOTmyv6Q7tMh"
auth = tw.OAuthHandler(key, key_secret, "oob")
auth.set_access_token(access_token, access_secret)
api = tw.API(auth)

global points


@app.route('/', methods=["GET"])
def index():
    return jsonify("Welcome to twitter scrapper")


@app.route('/tweets', methods=["GET"])
def get_tweets():
    args = request.args
    domain = args.get("domain", default="", type=str)
    tweets = list(tw.Cursor(
        api.search_tweets, "{0} in India ".format(domain), result_type='recent', tweet_mode='extended', count=50).items(50))
    Tweet_outpt = []
    for i in tweets:
        text = ""
        try:
            text = i._json['retweeted_status']['full_text'] if i.full_text.startswith(
                "RT @") else i.full_text
        except AttributeError:
            text = i.full_text
        place = ""
        if i.place:
            place = i.place.full_name
        json_output = {
            "Department": domain,
            "tweet": text,
            "tweet_associated_place": place,
            "tweeter_location": i.user.location,
            "Time_of_tweet": i.created_at,
            "User name": i.user.name,
        }
        Tweet_outpt.append(json_output)
    return jsonify(Tweet_outpt)
