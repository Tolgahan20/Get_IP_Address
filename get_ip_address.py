import socket

hostname = socket.gethostname()
IPAddress = socket.gethostbyname(hostname)

print(IPAddress)
