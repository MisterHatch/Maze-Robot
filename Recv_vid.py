import socket
import numpy as np
import cv2

UDP_IP = "192.168.80.128"
UDP_PORT1 = 5005
#UDP_PORT2 = 5006

sock1 = socket.socket(socket.AF_INET,
                socket.SOCK_DGRAM)
#ock2 = socket.socket(socket.AF_INET,
 #               socket.SOCK_DGRAM)

sock1.bind((UDP_IP,UDP_PORT1))
#sock2.bind((UDP_IP,UDP_PORT2))

while True:
        frstr, addr1 = sock1.recvfrom(63000)
        #imstr, addr2 = sock2.recvfrom(63000)
        frdata = np.fromstring(fstr,np.uint8)
        fr = np.reshape(frdata,(140,150,3))
        #imdata = np.fromstring(imstr,np.uint8)
       # im = np.reshape(imdata,(140,150,3))
        cv2.imshow('webcam',fr)
        #cv2.imshow('picam',im)
        cv2.waitKey(150)