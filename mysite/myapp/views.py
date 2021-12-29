from django.shortcuts import render
from django.http import FileResponse

import urllib3
import json
import subprocess

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

        if searchValue == '':
            return "Dont hack me :|"
        else:
            context = {'searchValue': searchValue, 
            'r' : json.loads((http.request('GET', f'http://localhost:8983/solr/nutch/select?&q={searchValue}')).data.decode("utf-8")),
            }
            return render(request, "search.html", context)
    else:
        return HttpResponse("u Hecker :(")

def flag(request):
    # command = 'ls'
    # print(subprocess.run(command, capture_output = True, text = True).stdout.split('\n'))
    img = open('indianFlag.png', 'rb')
    return FileResponse(img)

def icon(request):
    img = open('favicon.ico', 'rb')
    return FileResponse(img)
