from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models

BASE_CRAIGLIST_URL = 'https://bangalore.craigslist.org/search/jjj?query={}'
# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(new_search = search)
    final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
    response =requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features = 'html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})

    final_postings =[]

    for post in post_listings:
        post_titles =post.find(class_ = 'result-title').text
        post_url = post.find('a').get('href')

        if post.find(class_= 'result-price'):
            post_price = post.find(class_ = 'result-price').text
        else:
            post_price ='N/A'

        final_postings.append((post_titles, post_url, post_price))

    print(final_postings)
    stuff_for_frontend = {
        'search' : search,
        'final_postings': final_postings,
    }
    return render(request, 'myapp/new_search.html', stuff_for_frontend)