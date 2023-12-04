# import requests 

# x = requests.post("http://79.174.95.199:5000/auth/jwt/create/",data={"email":"ahmad.alhussinin@gmail.com","password":"1qaz2wsx3edcC"})
# print(x.content)
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 5000              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)