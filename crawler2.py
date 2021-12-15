import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
myIP = s.getsockname()[0]
print(myIP, end='\n')
s.close()

upIP = []

def hostScan():
    hostScanCommand = "nmap -sP "+myIP+"/24 " # -oG  - | awk '/Up$/{print $2}'"
    outputHostScanCommand = subprocess.run( hostScanCommand.split(), capture_output = True, text=True).stdout.split('\n')

    for lines in outputHostScanCommand:
        if 'up' in lines.split():
            IPLine = outputHostScanCommand[outputHostScanCommand.index(lines) - 1]
            upIP.append(IPLine.split()[-1])

def portScan():
    for ip in upIP:
        print(ip)
        openPorts = []
        # portScanCommand = 'nmap -n -p- '+ip
        # It'll took 4mins approx for scanning all ports in 1 IP
        # outputPortScanCommand = subprocess.run( portScanCommand.split(), capture_output = True, text = True)
        outputPortScanCommand = [ 
        'Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-15 09:18 IST',
        'Nmap scan report for 192.168.38.253',
        'Host is up (0.0016s latency).',
        'Not shown: 65534 closed tcp ports (conn-refused)',
        'PORT   STATE SERVICE',
        '53/tcp open  domain',
        '22/tcp open  ssh'
        ]

        for lines in outputPortScanCommand:
            if 'open' in lines.split():
                temp = lines.split()[0]
                port = temp.split('/')
                print(port[0])

hostScan()
portScan()
