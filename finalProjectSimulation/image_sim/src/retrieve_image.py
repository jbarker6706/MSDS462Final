#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String

from cv_bridge import CvBridge
import cv2

rospy.init_node('tb3_fetch_pub')
rospy.loginfo('tb3_fetch_pub started')
pub = rospy.Publisher('tb3type', String, queue_size=10)
tbtype=0
tb3Msg = "burger"

def process_image(msg):
    try:
        global tbtype
        # convert sensor_msgs/Image to OpenCV Image
        bridge = CvBridge()
        orig = bridge.imgmsg_to_cv2(msg, "bgr8")
        drawImg = orig
        # show results
        rospy.loginfo('process_image type = ' + str(tbtype))
        showImage(drawImg)
        if(tbtype%2==0):
            tb3Msg = "burger"
        else:
            tb3Msg = "waffle"
        pub.publish(tb3Msg)
        tbtype += 1
    except Exception as err:
        print err

def showImage(img):
    cv2.imshow('image', img)
    cv2.waitKey(1)

def start_node():
#    rospy.init_node('retrieve_image')
    rospy.loginfo('retrieve_image part of tb3_fetch_pub node started')
    rospy.Subscriber("image", Image, process_image)
    rospy.spin()

if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException:
        pass
