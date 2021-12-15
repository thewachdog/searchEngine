# https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/

import urllib3
import subprocess

print(subprocess.run(["ls", "-l"]))

http = urllib3.PoolManager()
r = http.request('GET', 'http://127.0.0.1:5500')
rawPageLines = r.data #.decode("utf-8"))
pageLine1 =  rawPageLines.splitlines()[0].decode('utf-8')
pageLine2 =  rawPageLines.splitlines()[1].decode('utf-8')

print(r.status)

'''
index1 = pageLine1.index('>')
print(pageLine1[index1 - 4: index1])
print(pageLine1)
index2 = pageLine2.index('<') + 1
print(pageLine2[index2:index2 + 4])
print(pageLine2)
'''

print(pageLine1, pageLine2[:5])
