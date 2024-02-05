# user input ip & port range

#declare ip & port range

#for x in port range
    #connect to ip with x
        #if no response retrun false
        #else return true

#print port range

import socket

port = []

ip = input("Enter ip to scan:")

userPort = input("Enter ports to scan:")

port2Scan = userPort.split()

for i in range(len(port2Scan)):
    port2Scan[i] = int(port2Scan[i])

for i in port2Scan:
    s = socket.socket()
    s.connect((ip, i))


