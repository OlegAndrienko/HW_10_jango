import json
from bson.objectid import ObjectId

from pymongo import MongoClient

client = MongoClient('mongodb+srv://olegandrienko:AOjktu1117@cluster.81vbs6u.mongodb.net/mongo_?retryWrites=true&w=majority')

db = client.hw_10_dj

with open('C:/Users/Oleg/OneDrive/GOIT_cloud/hw_10_dj/hw_10_dj/hw_10_django/utils/qoutes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)

# for quote in quotes:
#     print(quote)
    
for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    print(author)
    if author is not None:
        db.qoutes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tag'],
            # 'author': quote['author'],
            
            'author': ObjectId(author['_id']),
            
        })
        

