# nmap -sP 192.168.137.83/24 -oG - | awk '/Up$/{print $2}' > upHosts.txt


# import socket
import nmap

'''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
myIP = s.getsockname()[0]
# print(myIP)
s.close()

'''

nm = nmap.PortScanner()

file1 = open('upHosts.txt', 'r')
lines = file1.readlines()


for ip in lines:
    print(ip)
    # nm.scan(myIP, "22-443")
    # print(nm.scaninfo())
    for i in range(1,65535):
    # scan the target port
        print(i)
        res = nm.scan(ip,str(i))
    # the result is a dictionary containing
    # several information we only need to
    # check if the port is opened or closed
    # so we will access only that information
    # in the dictionary
        # print(res['state'])
        res = res['scan'][ip.strip('\n')]['tcp'][i]['state']
        # print(res['state'])
        # print(f"{res}")
        if f"{res}" == "open":
            print(f'port {i} is {res}.')
