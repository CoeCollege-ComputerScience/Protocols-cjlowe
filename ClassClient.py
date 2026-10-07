import socket
from socket import *

def simpleClient(host, message):
    s = socket()
    s.connect((host, 2001))
    s.send(message.encode("utf-8"))

    response = s.recv(1024)
    data = response.decode("utf-8")
    print(data)

    person = "all"
    message = "where " + person
    s.send(message.encode('utf-8'))

    response = s.recv(1024)
    data = response.decode("utf-8")
    print("*"+data)


    s.close()

def getMyIp():
    return "192.168.0.140"
    # return "172.16.212.159"

def getHostName():
    return "colton"

# print('colton,' + getMyIp())


# simpleClient("192.168.0.43", getHostName() + "," + getMyIp())
simpleClient("192.168.0.225", getHostName() + "," + getMyIp())
# simpleClient("192.168.0.43:2001", "what")
# simpleClient("192.168.0.43:2001", "where")
# simpleClient("192.168.0.43:2001", "when")
# simpleClient("192.168.0.43:2001", "why")
# simpleClient("192.168.0.43:2001", "how")

def getHost(hostName):
    simpleClient("192.168.0.225", "colton," + getMyIp())

