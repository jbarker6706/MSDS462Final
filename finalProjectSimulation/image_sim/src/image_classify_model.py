#!/usr/bin/python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

import numpy as np
from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions


class ImageClassifyModel():

    def __init__(self):
        self.model = load_model('vgg16_tb3_burger_waffle.h5')
        self.model,summary()
        self.image_class = ["tb3hamburger", "tb3waffle"]

 
    def classifyImage(image):
        orig = bridge.imgmsg_to_cv2(image, "bgr8")
        image_array = img_to_array(orig)
        image_array = image_array.reshape((1, image_array.shape[0], 
                      image_array.shape[1], image_array.shape[2]))
        image_array = preprocess_input(image_array)
        yhat = model.predict(image_array)
        msg = self.image_class[np.argmax(yhat)]
        return String(msg)

