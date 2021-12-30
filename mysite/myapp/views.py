from django.shortcuts import render
from django.http import FileResponse

import urllib3
import json
import subprocess
import re

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

        searchValue = re.sub(' +', ' ', searchValue)
        wordValidaton = re.compile(r'\w')

        final = ''

        for _ in searchValue:
            if re.match(wordValidaton, _) or _ == ' ':
                final += _

        # Store results ...
        http = urllib3.PoolManager()
        # resp = http.request('GET', f'http://localhost:8983/solr/nutch/select?q={searchValue}')
        # r = json.loads(resp.data.decode("utf-8"))
        # count = r['response']['numFound']

        if searchValue == '':
            return "Search what you want but don't hack me :|"
        else:
            print(final)
            context = {'searchValue': final, 
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
