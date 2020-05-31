# Client side
import socket
import pickle

HEADER_SIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8080)) #client want to connect so s.connect

msg =s.recv(1024)# buffer how bigger chunck data we want to recive at a time
print(msg.decode('utf-8')) #we are sendig and reciving message in bytes

