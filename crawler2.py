import socket
import subprocess
import urllib3
import urllib
import subprocess
from bs4 import BeautifulSoup
import requests

# def scrap(u):
#     links = []
#     def ScrapUrl(urlLink):
#         url = urlLink
#         try:
#             req = requests.get(url)
#             soup = BeautifulSoup(req.text,"html.parser")
#             #print(links)
#             newlink = 0
#             for link in soup.find_all('a'):
#                 l = link.get('href') # gets value from a:href in that html page
#                 print(l)
#                 if l:
#                     '''
#                     some ppl passing tokens nd othr values in links so it'll strip down that
#                     '''

#                     if ';' in l:
#                         l = l[:l.index(';')]

#                     if '#' in l and len(l) > 1:
#                         l = l[:l.index('#')]

#                     if '?' in l and len(l) > 1:
#                         l = l[:l.index('?')]

#                     if len(l) > 1:
#                         if (l[0] == '/' or urlLink == l[:len(urlLink)]) and l not in links:
#                             '''
#                             if its in same domain (same starts with '/')
#                             and unique (already found that link)+= 1
#                             '''
#                             print(l)
#                             links.append(l)
#                             newlink += 1
#             print(newlink)
#             if newlink == 0:
#                 return False

#             for l in links:
#                 print(l)
#                 ScrapUrl(f"{url}{l}")            
#         except Exception as e:
#             print(e)
#     ScrapUrl(u)

# def textCrawl():
#     print(subprocess.run(["ls", "-l"]))
#     http = urllib3.PoolManager()
#     r = http.request('GET', 'http://127.0.0.1:5500')
#     rawPageLines = r.data #.decode("utf-8"))
#     pageLine1 =  rawPageLines.splitlines()[0].decode('utf-8')
#     pageLine2 =  rawPageLines.splitlines()[1].decode('utf-8')
#     print()
#     print(r.status)
#     print(pageLine1, pageLine2[:5])

def hostScan():
    hostScanCommand = "nmap -sP "+myIP+"/24 " # -oG  - | awk '/Up$/{print $2}'"
    outputHostScanCommand = subprocess.run( hostScanCommand.split(), capture_output = True, text=True).stdout.split('\n')
    print(outputHostScanCommand)
    for lines in outputHostScanCommand:
        if 'up' in lines.split():
            IPLine = outputHostScanCommand[outputHostScanCommand.index(lines) - 1]
            #print(IPLine.split()[-1])
            if (IPLine.split()[-1]) != myIP:
                upIP.append(IPLine.split()[-1])

def portScan():
    for ip in upIP:
        print(ip)
        openPorts = []
        portScanCommand = 'nmap -n -p- '+ip
        # It'll took 4mins approx for scanning all ports in 1 IP
        '''
        outputPortScanCommand = [
        'Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-15 09:18 IST',
        'Nmap scan report for 192.168.38.253',
        'Host is up (0.0016s latency).',
        'Not shown: 65534 closed tcp ports (conn-refused)',
        'PORT   STATE SERVICE',
        '5500/tcp open  domain',
        #'22/tcp open  ssh'
        ]
        '''
        outputPortScanCommand = subprocess.run( portScanCommand.split(), capture_output = True, text = True).stdout.split('\n')
        print(outputPortScanCommand)
        for lines in outputPortScanCommand:
            if 'open' in lines.split():
                temp = lines.split()[0]
                port = temp.split('/')
                print(port[0])
                # r = http.request('GET',f"http://{ip}:{port[0]}")
                http = urllib3.PoolManager()
                try:
                    r = http.request('GET', f'http://{ip}:{port[0]}', timeout = 5) # what will happen if server doesn't responds ? Timeout fixed .
                    if r.status == 200:
                        # it'll return all the subdomains in the ip:port
                        # scrap(f'http://{ip}:{port[0]}') [No need for it, used Nutch          
                        # Write in the search/nutch/seed.txt file (for the Nutch to crawl) 
                        file1 = open('search/nutch/urls/seed.txt', 'a') # need to create this file beforehand
                        file1.writelines(f'http://{ip}:{port[0]}')
                        file1.close()
                except:
                    pass


                    # rawPageLines = r.data
                    # print(rawPageLines)
                    # pageLine1 =  rawPageLines.splitlines()[0].decode('utf-8')
                    
                    # if pageLine1 == "<!DOCTYPE html>" or pageLine1 == "<html":
                    #     print(f"{ip}:{port[0]} is a HTML Webpage")
                    #     # HTML fn using beautifulSoup
                    #     # textFn
                    # else:


# Main fn starts here

# To find my IP and system private network
http = urllib3.PoolManager()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
myIP = s.getsockname()[0]
print(myIP)
s.close()

upIP = []

hostScan()
portScan()
   