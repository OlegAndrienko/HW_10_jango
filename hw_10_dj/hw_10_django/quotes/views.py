from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from .utils import get_mongodb

def main(request, page_number=1):
    db = get_mongodb()
    quotes = db.qoutes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page_number)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})
