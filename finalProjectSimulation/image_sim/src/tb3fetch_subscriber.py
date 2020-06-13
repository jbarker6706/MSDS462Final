#!/usr/bin/env python


import rospy
from std_msgs.msg import String

from geometry_msgs.msg import Twist, Vector3
from math import pi


pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move = Twist()

def burgergo():
    move.linear.x = 0.2
    move.linear.y = 0.0
    duration = 5
    pub.publish(move)
    rospy.sleep(duration)
    move.linear.x = 0.0
    move.linear.y = 0.0
    pub.publish(move)

def wafflego():
    move.linear.x = 0.2
    move.linear.y = 0.0
    duration = 7
    pub.publish(move)
    rospy.sleep(duration)
    move.linear.x = 0.0
    move.linear.y = 0.0
    pub.publish(move)


def rotate90():
    move.linear.x = 0.0
    move.linear.y = 0.0
    duration = 10
    move.angular.z = pi*2/4/duration
    pub.publish(move)
    rospy.sleep(duration)
    move.angular.z = 0
    pub.publish(move)

def callback(msg):
    print msg.data
    if(msg.data == "burger"):
        burgergo()
        rotate90()
        print "get " + msg.data
        rotate90()
        burgergo()
        rotate90()
        rotate90()
    else:
        wafflego()
        rotate90()
        print "get " + msg.data
        rotate90()
        wafflego()
        rotate90()
        rotate90()


rospy.init_node('tb3fetch_subscriber')

sub = rospy.Subscriber('tb3type', String, callback)

rospy.spin()
