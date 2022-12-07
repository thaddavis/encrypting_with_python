import socket
from cryptography.fernet import Fernet

host='192.168.1.40'
port=12345

msg='White green black fox'

file=open('key.key', 'rb')
key=file.read()
# print(key)

encodedMsg = msg.encode()
f = Fernet(key)
encryptedMsg = f.encrypt(encodedMsg)

print(encryptedMsg)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))
# s.sendall(bytes(encryptedMsg, 'utf-8'))
s.sendall(encryptedMsg)