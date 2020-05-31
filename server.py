#creating sockets from scratch again
import socket
import pickle
import time





HEADER_SIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET corresponds to ipv4 and SOCK_STREAM corresponds to  TCP
s.bind(('127.0.0.1', 8080)) # basically localhost:1234
s.listen(5) 

while True:
    clientsocket, address = s.accept()
    print(f'Connection form {address} has been established!')

    msg = "welcome mother fuckers"
    msg = "711"+msg #header
    clientsocket.send(bytes(msg, 'utf-8'))

   # 'while True:
   #      time.sleep(3)
   #      msg = f"The time is! {time.time}"
   #      msg = "711"+msg #header
   #      clientsocket.send(bytes(msg, "utf-8"))

