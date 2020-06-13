#!/usr/bin/env python
import rospy

import sys
import cv2
import os

from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        dim = (224, 224)
        # resize image
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        if img is not None:
            images.append(resized)
    return images

waffles = []
hamburgers = []

def start_node():
    rospy.init_node('image_sim_pub')
    rospy.loginfo('image_sim_pub node started')
    waffledir = "/home/jbarker6706/Documents/MSDS462/assignment8/train/tb3waffle/"
    waffles = load_images_from_folder(waffledir)
    hamburgerdir = "/home/jbarker6706/Documents/MSDS462/assignment8/train/tb3hamburger/"
    hamburgers = load_images_from_folder(hamburgerdir)
    icnt = 0
    bridge = CvBridge()
    pub = rospy.Publisher('image', Image, queue_size=10)
    while not rospy.is_shutdown():
        imgMsg = bridge.cv2_to_imgmsg(waffles[icnt%len(waffles)], "bgr8")
        if(imgMsg != None):     
            pub.publish(imgMsg)
        rospy.sleep(10)  # 1 Hz
        imgMsg = bridge.cv2_to_imgmsg(hamburgers[icnt%len(hamburgers)], "bgr8")    
        if(imgMsg != None):     
            pub.publish(imgMsg)
        rospy.sleep(10)  # 1 Hz
        ++icnt

if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException:
        pass

