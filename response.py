#!/usr/bin/env python

import urllib3
import json


http = urllib3.PoolManager()

# url = 'http://localhost:8983/solr/nutch/select?q=apache'
# resp = http.request('GET', url)
searchValue = 'apache'
url = f'http://localhost:8983/solr/nutch/select?q={searchValue}'
print(url)
resp = http.request('GET', url)

# print(resp.headers['Server'])
# print(resp.headers['Date'])
# print(resp.headers['Content-Type'])
# print(resp.headers['Last-Modified'])
r = json.loads(resp.data.decode("utf-8"))
print(r['responseHeader'])
print(r['response']['numFound'])