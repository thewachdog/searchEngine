from django.shortcuts import render

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
    context = {
	'searchValue': searchValue
    }
    return render(request, "search.html", context)
