#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

from std_msgs.msg import String
import tensorflow as tf

import numpy as np
from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions

#from image_classify_model import ImageClassifyModel

config = tf.ConfigProto(
device_count={'GPU': 1},
intra_op_parallelism_threads=1,
allow_soft_placement=True
)

config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction = 0.6

session = tf.Session(config=config)
tf.keras.backend.set_session(session)

# load model
model = load_model('vgg16_tb3_burger_waffle.h5')
model._make_predict_function()
model.summary()

image_class = ["tb3hamburger", "tb3waffle"]

def classify_image(image):
    print("first")
    print(type(image))
    bridge = CvBridge()
    orig = bridge.imgmsg_to_cv2(image, "bgr8")

    image_array = img_to_array(orig)
    print("second")
    image_array = image_array.reshape((1, image_array.shape[0], 
                  image_array.shape[1], image_array.shape[2]))
    print("third")
    image_array = preprocess_input(image_array)
    print("fourth")
    yhat = model.predict(image_array)
    print("last")
    print(yhat)
    return image_class[np.argmax(yhat)]

def process_image(msg):
    try:
        # convert sensor_msgs/Image to OpenCV Image
        #bridge = CvBridge()
        #orig = bridge.imgmsg_to_cv2(msg, "bgr8")
        #drawImg = orig
        # show results
        #showImage(drawImg)
        print("First")
        classmsg = classify_image(msg)
        print("Last")
        print classmsg
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
