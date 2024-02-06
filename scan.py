import socket

port = []

ip = input("Enter ip to scan:")

userPort = input("Enter ports to scan:")

port2Scan = userPort.split()

for port in range(len(port2Scan)):
    port2Scan[port] = int(port2Scan[port])

for port in port2Scan:
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        print("Connected on port: " + str(port))
    except:  
        print("Couldn't connect on port: " + str(port))


