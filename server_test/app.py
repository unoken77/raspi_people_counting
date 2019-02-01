# -*- coding:utf-8 -*-

from bottle import route, run, template, request, static_file
import cv2
cap=cv2.VideoCapture(0)
@route('/hello')
def hello():
    return "Hello World!"
@route('/')
def index():
	return template('index')
	
#@route('/image')
@route('/<filename:path>')
def static(filename):
	ret, frame = cap.read()
	print('took')
	cv2.imwrite('/home/pi/Desktop/server_test/images/image.jpg', frame)
	return static_file(filename, root="./images")
    
run(host='192.168.1.83', port=8080, debug=True)
