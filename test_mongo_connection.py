import pymongo
import certifi
import spacy


nlp = spacy.load("pt_core_news_lg")

from pymongo import MongoClient 


client = pymongo.MongoClient("mongodb+srv://bruno:bruno87bmt@cluster0.dvoa7.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = client.test

db = client["SmartLex"]

collection = db["posts_with_meta_clean"]

x = collection.find_one()

print()

# Process a text
doc = nlp(x["post_content"])
print(doc.text)
print("---")
for ent in doc.ents:
    print(ent.text, ent.label_)

print(spacy.explain("MISC"))
# for x in collection.find():
# print(x)