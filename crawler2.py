import subprocess
import urllib3
import urllib
import subprocess
from bs4 import BeautifulSoup
import requests

def hostScan():
    hostScanCommand = "nmap -sP "+myIP+"/24"# -oG  - | awk '/Up$/{print $2}'"
    outputHostScanCommand = subprocess.run( hostScanCommand.split() , capture_output = True, text=True).stdout.split('\n')
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
        portScanCommand = 'nmap -n -p- -T4 -Pn '+ip
        # It'll took 4mins approx for scanning all ports in 1 IP

        outputPortScanCommand = subprocess.run( portScanCommand.split() , capture_output = True, text = True).stdout.split('\n')
        print(outputPortScanCommand)
        for lines in outputPortScanCommand:
            if 'open' in lines.split():
                temp = lines.split()[0]
                port = temp.split('/')
                print(port[0])
                http = urllib3.PoolManager()
                try:
                    r = http.request('GET', f'http://{ip}:{port[0]}', timeout = 5)
                    if r.status == 200:          
                        # Write in the search/nutch/seed.txt file (for the Nutch to crawl) 
                        file1 = open('search/nutch/urls/seed.txt', 'a') # need to create this file beforehand
                        file1.writelines(f'http://{ip}:{port[0]}\n')
                        file1.close()
                except:
                    pass

# Main fn starts here

# To find my IP and system private network

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(("8.8.8.8", 80))
# myIP = s.getsockname()[0]
# print(myIP)
# s.close()

# cmd = 'hostname -I'
# myIP = subprocess.run(cmd.split() , capture_output = True, text = True).stdout.split()[0]

file1 = open('ip.txt', 'r')
myIP = ''
Lines = file1.readlines()
for line in Lines:
    print(line.strip())
    myIP = line.split()[0]
    break
print(myIP)
file1.close()

upIP = []

hostScan()
portScan()
   