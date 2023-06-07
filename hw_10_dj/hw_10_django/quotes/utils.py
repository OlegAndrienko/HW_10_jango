from pymongo import MongoClient
from bson.objectid import ObjectId
import json


def get_mongodb():
    client = MongoClient('mongodb+srv://olegandrienko:AOjktu1117@cluster.81vbs6u.mongodb.net/mongo_?retryWrites=true&w=majority')
    db = client.hw_10_dj
    return db