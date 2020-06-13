#!/usr/bin/env python

import rospy

#from image_classify_model import ImageClassifyModel

from image_sim.srv import ImageClassify,ImageClassifyResponse
from image_sim.srv import ImageClassifyRequest

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

model = load_model('vgg16_tb3_burger_waffle.h5')
model.summary()
image_class = ["tb3hamburger", "tb3waffle"]
bridge = CvBridge()

def classify(request):
    orig = bridge.imgmsg_to_cv2(request.imgmsg, "bgr8")
    image_array = img_to_array(orig)
    image_array = image_array.reshape((1, image_array.shape[0], 
                  image_array.shape[1], image_array.shape[2]))
    image_array = preprocess_input(image_array)
    drawImg = orig
    # show results
    showImage(drawImg)

#    yhat = model.predict(image_array)
#    msg = self.image_class[np.argmax(yhat)]
    msg = "hamburger"
    return String(msg)
#    my_classifier = ImageClassifyModel        
#    return ImageClassifyResponse(my_classifier.classifyImage(request))

def showImage(img):
    cv2.imshow('image', img)
    cv2.waitKey(1)

rospy.init_node('image_classifier_service')
service = rospy.Service('image_classify', ImageClassify, classify)

rospy.spin()
