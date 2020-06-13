#!/usr/bin/python

import rospy
import sys
from turtlebot3_logic import RosTurtlebotLogic


def loadParams():
    forwardSpeed = 100
    rotationSpeed = 10
    minDistanceFromObstacle = 1.0
    minimumAngle = -30
    maximumAngle = 30

    if rospy.has_param('~forward_speed'):
        forwardSpeed = rospy.get_param('~forward_speed')
        print("fs")
    if rospy.has_param('~rotation_speed'):
        rotationSpeed = rospy.get_param('~rotation_speed')
        print("rs")
    if rospy.has_param('~minimum_distance_from_obstacle'):
        minDistanceFromObstacle = rospy.get_param('~minimum_distance_from_obstacle')
        print("mindis")
    if rospy.has_param('~minimum_angle'):
        minimumAngle = rospy.get_param('~minimum_angle')
        print("minang")
    if rospy.has_param('~maximum_angle'):
        maximumAngle = rospy.get_param('~maximum_angle')
        print("maxang")

    return forwardSpeed, rotationSpeed, minDistanceFromObstacle, minimumAngle, maximumAngle


if __name__ == "__main__":
    rospy.loginfo("Started program.")

    rospy.init_node("stopper_node", argv=sys.argv)
    forwardSpeed, rotationSpeed, minDistanceFromObstacle, minimumAngle, maximumAngle = loadParams()
    rospy.loginfo("Finished import parameters.")
    
    #print(forwardSpeed, rotationSpeed, minDistanceFromObstacle, minimumAngle, maximumAngle)

    my_stopper = RosTurtlebotLogic(forwardSpeed, rotationSpeed, minDistanceFromObstacle, minimumAngle, maximumAngle)
    my_stopper.startMoving()
