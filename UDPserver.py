
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('ready')

while True:
    msg, clientAddr = serverSocket.recvfrom(2048)
    print(msg)
    modifyMsg = msg.upper()
    serverSocket.sendto(modifyMsg, clientAddr)
