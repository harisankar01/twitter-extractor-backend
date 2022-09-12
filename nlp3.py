import spacy


def nlp(doc):
    nlp_wk = spacy.load('xx_ent_wiki_sm')
    doc = nlp_wk(doc.replace("#", " "))
    places = []
    for token in doc:
        if token.ent_type_ == "LOC":
            places.append(token.text)
    return " ".join(places)
