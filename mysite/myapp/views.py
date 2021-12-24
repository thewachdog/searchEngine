from django.shortcuts import render

import urllib3
import json

# Create your views here. (WTF IS VIEWS ????)
from django.http import HttpResponse

def index(request):
#    text = """<h1>welcome to my app !</h1>"""
#    return HttpResponse(text)
    return render(request, "index.html", {})

def search(request):
#    text = "Displaying article Number : %s" % searchValue
#    return HttpResponse(text)
    if request.GET:
        searchValue = request.GET['searchValue']


        # Store results ...
        http = urllib3.PoolManager()
        # resp = http.request('GET', f'http://localhost:8983/solr/nutch/select?q={searchValue}')
        # r = json.loads(resp.data.decode("utf-8"))
        # count = r['response']['numFound']


        context = {'searchValue': searchValue, 
        'r' : json.loads((http.request('GET', f'http://localhost:8983/solr/nutch/select?q={searchValue}')).data.decode("utf-8")),
        }
        if searchValue == '':
            return "u r Hecker :-("
        else:
            return render(request, "search.html", context)
    else:
        return HttpResponse("u Hecker :(")
