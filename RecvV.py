import socket
import numpy as np
import cv2

UDP_IP = "Alpha.byod.gmu.edu"
UDP_PORT = 5010

sock = socket.socket(socket.AF_INET,
                socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while True:
        data, addr = sock.recvfrom(40000)
        #Convert string to image data
        imgdata = np.fromstring(data,np.uint8)
        #Reshape image data to proper size
        img = np.reshape(imgdata,(200,200))
        cv2.imshow('image',img)
        cv2.waitKey(150)
