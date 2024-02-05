import socket

port = []

ip = input("Enter ip to scan:")

userPort = input("Enter ports to scan:")

port2Scan = userPort.split()

for i in range(len(port2Scan)):
    port2Scan[i] = int(port2Scan[i])

for i in port2Scan:
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, i))
        print("Connected on port: " + str(i))
    except:  
        print("Couldn't connect on port: " + str(i))


