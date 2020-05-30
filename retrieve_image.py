#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def process_image(msg):
    try:
        # convert sensor_msgs/Image to OpenCV Image
        bridge = CvBridge()
        orig = bridge.imgmsg_to_cv2(msg, "bgr8")
        drawImg = orig
        # show results
        showImage(drawImg)
    except Exception as err:
        print err

def showImage(img):
    cv2.imshow('image', img)
    cv2.waitKey(1)

def start_node():
    rospy.init_node('retrieve_image')
    rospy.loginfo('retrieve_image node started')
    rospy.Subscriber("image", Image, process_image)
    rospy.spin()

if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException:
        pass
