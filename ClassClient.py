import socket
# from socket import *

print("Ip: " + socket.gethostbyname(socket.gethostname()))


def getMyIp():
    print("Ip: " + socket.gethostbyname(socket.gethostname()))
    return socket.gethostbyname(socket.gethostname())


def getHostName():
    return "colton"

def simpleClient(host, message, protocol):
    s = socket.socket()
    s.connect((host, protocol))

    if protocol == 2001:
        message = getHostName() + "," + getMyIp()
        print(message)
        s.send(message.encode("utf-8"))
        response = s.recv(1024)
        data = response.decode("utf-8")
        print(data)
        message = "where " + message
        s.send(message.encode('utf-8'))
        response = s.recv(1024)
        data = response.decode("utf-8")
        print("*"+data)
        s.close()
        return (data.split(","))[0]
    elif protocol == 2026:
        s.send(message.encode("utf-8"))
        response = s.recv(1024)
        data = response.decode("utf-8")
        print(data)
        s.close()
        return ""
    return ""

def LearnAbout(hostName):
    personIP = simpleClient("192.168.0.43", hostName, 2001)
    simpleClient(personIP, "what", 2026)
    simpleClient(personIP, "where", 2026)
    simpleClient(personIP, "when", 2026)
    simpleClient(personIP, "why", 2026)
    simpleClient(personIP, "how", 2026)

LearnAbout("hughes")


