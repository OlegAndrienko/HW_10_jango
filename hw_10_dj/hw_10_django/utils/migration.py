import os
import django

from pymongo import MongoClient


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_10_django.settings")
django.setup()

from quotes.models import Quote, Author, Tag

client = MongoClient('mongodb+srv://olegandrienko:AOjktu1117@cluster.81vbs6u.mongodb.net/mongo_?retryWrites=true&w=majority')

db = client.hw_10_dj

authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        discription=author['discription'],
    )
 
quotes = db.qoutes.find()

for quote in quotes:
    # quote_obj = Quote.objects.get_or_create(
    #     quote=quote['quote'],
    #     author=Author.objects.get(fullname=quote['author']),
    # )[0]
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)
      
    exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))
 
    if not exist_quote:
        author = db.authors.find_one({'_id': quote['author']})
        a = Author.objects.get(fullname=author['fullname'])
        quote_obj = Quote.objects.create(
            quote=quote['quote'],
            author=a,
        )
        for tag in tags:
            quote_obj.tags.add(tag)