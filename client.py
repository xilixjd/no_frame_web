

from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = 'abc'
clientSocket.sendto(message.encode(encoding='utf-8'), (serverName, serverPort))
modifiedMsg, serverAddr = clientSocket.recvfrom(2048)
print(modifiedMsg)
clientSocket.close()