from socket import *
from datetime import datetime



def SimpleServer():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    ip = "127.0.0.1"
    #ip = "192.168.0.225"
    s.bind((ip, 2026))
    s.listen()

    while True:
        conn, addr = s.accept()
        msg = conn.recv(1024).decode('utf-8')
        print(msg)
        print(f"Connected by {addr}")
        conn.send(WWWWWProtocol(msg, ip).encode("utf-8"))
        conn.close()

def WWWWWProtocol(inputString, ip):
    time = datetime.now()
    if inputString == "who":
        return "I am Groot"
    elif inputString == "what":
        return "Command Server 2026"
    elif inputString == "when":
        return time.strftime("%H:%M:%S")
    elif inputString == "where":
        return ip
    elif inputString == "why":
        return "because"
    else:
        return "I'm sorry Dave, I can't do that"

SimpleServer()