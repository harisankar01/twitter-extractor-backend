import twint
import re
from dotenv import load_dotenv
from flask import Flask, jsonify, request
import tweepy as tw
load_dotenv()
app = Flask(__name__)
# ENV vars
key = "JbYaDTbeBLA1svw8N0rbW9AWc"
key_secret = "8HOFGU54XuVO7JTPjmM6YXLuxweizpdSKs1NQ5MrFWl8KIplki"
access_token = "1438353997765623812-z5JipdSMKkfM1RlwGktOAnzZ7r7E1q"
access_secret = "PJN3D7IiW2ZdI6QddzoLd3iKb7GwxZIkW0drixv2uYX12"
auth = tw.OAuthHandler(key, key_secret, "oob")
auth.set_access_token(access_token, access_secret)
api = tw.API(auth)

global points

# Test route


@app.route('/', methods=["GET"])
def index():
    return jsonify("Welcome to twitter scrapper")

# Get tweets from twitter


@app.route('/tweets', methods=["GET"])
def get_tweets():
    args = request.args
    domain = args.get("domain", default="", type=str)
    tweets = list(tw.Cursor(
        api.search_tweets, "{0}".format(domain), result_type='latest', tweet_mode='extended', count=20, lang="en").items(20))
    # print(tweets)
    Tweet_outpt = []
    tweet__list = []
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
        url = re.search(r"http\S+", text)
        try:
            url = url.group(0)
        except AttributeError:
            url = "Not available"
        converted = ' '.join(
            re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split()).lower()
        if converted in tweet__list:
            continue
        tweet__list.append(converted)
        text = re.sub(r"(?:\@|https?\://)\S+", "", text)
        json_output = {
            "Department": domain,
            "tweet": text,
            "tweet_associated_place": place,
            "Time_of_tweet": i.created_at,
            "User name": i.user.screen_name,
            "Associated_url": url,
            "tweeter_location": i.user.location,
            "Priority": 0,
            "id": i.user.id
        }
        Tweet_outpt.append(json_output)
    return jsonify(Tweet_outpt)


@app.route("/emergency", methods=["GET"])
def emer():
    cities = ["Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha",
              "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]
    final_tweet = []
    for j in cities:
        tweets = list(tw.Cursor(
            api.search_tweets, "accidents in {0}".format(j), result_type='latest', tweet_mode='extended', count=10, lang="en").items(7))
        # print(tweets)
        Tweet_outpt = []
        tweet__list = []
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
            url = re.search(r"http\S+", text)
            try:
                url = url.group(0)
            except AttributeError:
                url = "Not available"
            converted = ' '.join(
                re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split()).lower()
            if converted in tweet__list:
                continue
            tweet__list.append(converted)
            text = re.sub(r"(?:\@|https?\://)\S+", "", text)
            if "fire" in text:
                domain = "Fire"
            elif "accident" in text:
                domain = "accidents"
            elif "pollution" in text:
                domain = "pollution"
            elif "incident" or "complaint" or "problem" in text:
                domain = "complaints"
            json_output = {
                "Department": domain,
                "tweet": text,
                "tweet_associated_place": j.upper(),
                "Time_of_tweet": i.created_at,
                "User name": i.user.screen_name,
                "Associated_url": url,
                "tweeter_location": i.user.location,
                "Priority": 0,
                "id": i.user.id
            }
            Tweet_outpt.append(json_output)
        final_tweet.append(Tweet_outpt)
    return jsonify(final_tweet)


@app.route("/complaints", methods=["GET"])
def complaints():
    cities = ["Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha",
              "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]
    final_tweet = []
    for j in cities:
        tweets = list(tw.Cursor(
            api.search_tweets, "police complaints in {0}".format(j), result_type='latest', tweet_mode='extended', count=10, lang="en").items(7))
        # print(tweets)
        Tweet_outpt = []
        tweet__list = []
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
            url = re.search(r"http\S+", text)
            try:
                url = url.group(0)
            except AttributeError:
                url = "Not available"
            converted = ' '.join(
                re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split()).lower()
            if converted in tweet__list:
                continue
            tweet__list.append(converted)
            text = re.sub(r"(?:\@|https?\://)\S+", "", text)
            json_output = {
                "Department": "complaints",
                "tweet": text,
                "tweet_associated_place": j.upper(),
                "Time_of_tweet": i.created_at,
                "User name": i.user.screen_name,
                "Associated_url": url,
                "tweeter_location": i.user.location,
                "Priority": 0,
                "id": i.user.id
            }
            Tweet_outpt.append(json_output)
        final_tweet.append(Tweet_outpt)
    return jsonify(final_tweet)


@app.route("/info", methods=["GET"])
def get_info():
    args = request.args
    name = args.get("name", default="", type=str)
    output = []
    output.append(api.get_user(name))
    return jsonify()


@app.route("/user", methods=["GET"])
def user():
    all_tweets = []
    Tweet_outpt = []
    args = request.args
    name = args.get("name", default="", type=str)
    tweets = api.user_timeline(screen_name=name,
                               count=20,
                               include_rts=False,
                               tweet_mode='extended'
                               )
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
        url = re.search(r"http\S+", text)
        try:
            url = url.group(0)
        except AttributeError:
            url = "Not available"
        converted = ' '.join(
            re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split()).lower()
        if converted in all_tweets:
            continue
        all_tweets.append(converted)
        text = re.sub(r"(?:\@|https?\://)\S+", "", text)
        json_output = {
            "tweet": text,
            "tweet_associated_place": place,
            "Time_of_tweet": i.created_at,
            "User name": i.user.screen_name,
            "Associated_url": url,
            "tweeter_location": i.user.location,
            "Priority": 0,
            "id": i.user.id,
            "tweet_id": i.id
        }
        Tweet_outpt.append(json_output)
    return jsonify(Tweet_outpt)


@app.route('/followers', methods=["GET"])
def get_user():
    args = request.args
    domain = args.get("name", default="", type=str)
    output = []
    print(api.get_user(screen_name=domain))
    for follower in tw.Cursor(api.get_follower_ids, screen_name=domain).items(30):
        val = api.get_user(user_id=follower)
        output.append(val.screen_name)
    return jsonify(output)


@app.route('/comments', methods=["GET"])
def get_replies():

    user_name = "Athiban_32"
    replies = tw.Cursor(api.search_tweets, q='to:{}'.format(user_name),
                        since_id="963825336373821440", tweet_mode='extended').items()
    while True:
        reply = replies.next()
        if not hasattr(reply, 'in_reply_to_status_id_str'):
            continue
        if reply.in_reply_to_status_id == "963825336373821440":
            print("reply of tweet:{}".format(reply.full_text))

    return jsonify("da")
