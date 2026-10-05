from socket import *

def simpleClient(host, message):
    s = socket()
    s.connect((host, 2026))
    s.send(message.encode("utf-8"))

    response = s.recv(1024)
    data = response.decode("utf-8")
    print(data)
    s.close()

simpleClient("127.0.0.1", "who")
simpleClient("127.0.0.1", "what")
simpleClient("127.0.0.1", "where")
simpleClient("127.0.0.1", "when")
simpleClient("127.0.0.1", "why")
simpleClient("127.0.0.1", "how")

