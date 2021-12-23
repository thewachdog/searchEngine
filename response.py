#!/usr/bin/env python

import urllib3
import json


http = urllib3.PoolManager()

url = 'http://localhost:8983/solr/nutch/select?q=nutch'
resp = http.request('GET', url)

# print(resp.headers['Server'])
# print(resp.headers['Date'])
# print(resp.headers['Content-Type'])
# print(resp.headers['Last-Modified'])
y = json.loads(resp.data.decode("utf-8"))
print(y['responseHeader'])
print(y['response']['numFound'])