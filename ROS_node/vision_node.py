#!/usr/bin/env python

import cv2
import rospy
from std_msgs.msg import String
import numpy as np

class imageRead(object):
    def __init__(self):
        rospy.init_node('vision_node', anonymous=True)
        self.stream_addr = 'http://192.168.0.20/video.cgi'
        self.cap = cv2.VideoCapture(self.stream_addr)
        self.ret, self.frame = self.cap.read()
        self.sub = rospy.Subscriber("vision_data", String, self.callback)
        self.timer = rospy.Timer(rospy.Duration(2), self.timer_callback)
        self.started = False
        rospy.spin()
    def callback(self,data):
        rospy.loginfo("Callback")
        if not self.started:
            self.started = True

    def timer_callback(self,event):
        if self.started:
            self.write_to_file()
            rospy.sleep(1.0)
    def write_to_file(self):
        rospy.loginfo("Writing...")
        while self.ret:
            with open('/mnt/hgfs/VMshared/images.jpg', 'w') as file:
                self.cap = cv2.VideoCapture(self.stream_addr)
                self.ret,self.frame = self.cap.read()
                cv2.imwrite("/mnt/hgfs/VMshared/images.jpg", self.frame)        
                rospy.loginfo("Written file")
	
if __name__ == '__main__':
    imageRead()