# coding: UTF-8

#!/usr/bin/python3           # This is server.py file
import socket
import cv2
import numpy
path="/home/pi/Desktop/current_number_of_people.txt"
print('start server')

# create a socket object
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
#host = socket.gethostname()
host = "192.168.1.59"
count=0

port = 9999

# bind to the port
serversocket.bind((host, port))
s='test'
send_pic=None
# queue up to 5 requests
serversocket.listen(5)
print('waiting connection...')
clientsocket, addr = serversocket.accept()
print("Got a connection from %s" % str(addr))
while True:
	msg=clientsocket.recv(1024)
	cap=cv2.VideoCapture(1)
	#OpenCVでWebカメラの画像を取り込む
	ret, frame = cap.read()
	frame=cv2.resize(frame, dsize=(200,200))
	frame=frame.tostring()
	clientsocket.send(frame)
	cap.release()
    #order=
    #clientsocket.send(s.encode('ascii'))
    #clientsocket.close()
clientsocket.close()
