#!/usr/bin/python

import math
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class RosTurtlebotLogic(object):

    def __init__(self, forwardSpeed, rotationSpeed, minDistanceFromObstacle, minimumAngle, maximumAngle):
        self.forwardSpeed = forwardSpeed
        self.rotationSpeed = rotationSpeed
        self.minDistanceFromObstacle = minDistanceFromObstacle

        # Keeps the current minimum distance from obstacle from laser.
        self.minimumRangeAhead = 5
        # In which direction to rotate, left or right.
        self.rotationDirection = .1
#        self.minimumIndexLaser = 360 * (90 + minimumAngle) / 90
#        self.maximumIndexLaser = 360 * (90 + maximumAngle) / 90 - 1
        self.minimumIndexLaser = 0
        self.maximumIndexLaser = 358
        self.keepMoving = True

       # self.commandPub = rospy.Publisher("/cmd_vel_mux/input/teleop", Twist, queue_size=10)
        self.commandPub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        rospy.Subscriber("scan", LaserScan, self.scanCallback, queue_size=10)

    def startMoving(self):
        rate = rospy.Rate(10)
        count = 0

        while(not rospy.is_shutdown()):
            if(self.keepMoving):
                if (self.minimumRangeAhead < self.minDistanceFromObstacle):
                    #print("I am GROOT <")
                    self.keepMoving = False
            else:
                if(self.minimumRangeAhead > self.minDistanceFromObstacle):
                    #print("I am GROOT >")
                    self.keepMoving = True

            twist = Twist()
            if(self.keepMoving):
                #print("I am GROOT x")
                twist.linear.x = self.forwardSpeed
                twist.angular.z = 0
            else:
                #print("I am GROOT z")
                if(count%2==0):
                    twist.angular.z = self.rotationDirection
                    twist.linear.x = 0
                else:
                    twist.angular.z = 0
                    twist.linear.x = 0

                self.keepMoving = True
            print(twist.linear.x, twist.angular.z)

            self.commandPub.publish(twist)
            rate.sleep()

    def scanCallback(self, scan_msg):
        minimum = 100
        index = 0
        
        # Find the minimum distance to obstacle and we keep the minimum distance and the index.
        # We need the minimum distance in order to know if we can go forward or not.
        # We need the index to know in which direction to rotate.
        if(not math.isnan(scan_msg.ranges[self.minimumIndexLaser])):
            minimum = scan_msg.ranges[self.minimumIndexLaser]

        for i in range(self.minimumIndexLaser, self.maximumIndexLaser + 1):
            if(not math.isnan(scan_msg.ranges[i]) and scan_msg.ranges[i] < minimum):
                minimum = scan_msg.ranges[i]
                index = i

        self.minimumRangeAhead = minimum

        if(index <= 359):
            self.rotationDirection = self.rotationSpeed
        else:
            self.rotationDirection = -self.rotationSpeed
