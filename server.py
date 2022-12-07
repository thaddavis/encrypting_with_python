import socket
from cryptography.fernet import Fernet

host='192.168.1.40'
port=12345

file = open('key.key', 'rb')
key = file.read()
file.close()

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

sock.listen(5)

while True:
    connection, address = sock.accept()
    buffer = connection.recv(1024)
    print(buffer)
    f = Fernet(key)
    decryptedMsg = f.decrypt(buffer)
    print(decryptedMsg)
    connection.send(buffer)
    connection.close()

