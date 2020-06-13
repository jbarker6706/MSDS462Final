# MSDS462Final
462 final project repository
Reference used for the publisher and subscriber topic files
Quigley, M. (2015). Programming Robots with ROS. Sebastopol, CA: O'Reilly Media Inc.


Added section to Jupyter file explaining how to add turtlebot3 to a ROS framework
Many thanks to Automatic Addison

May 22, 2020
Built VGG16 fine-tuned model to classify hamburger or waffle turtlebot3

May 30, 2020

Also added wandering turtlebot code which needs work. Thank you stckoverflow.

June 5, 2020
Added working version of wandering bot
Added utilities for redirecting trapped bot

June 12, 2020

Added final version of project as it pertains to MSDS462 includes camera sim, image retreive and classify, and fetch object scripts
To start the bot project from a ROS framework environment melodic with turtlebot3 simulation. From an Ubuntu terminal execute
The scripts for are located in 
roscore

roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch

rosrun image_sim image_sim_pub.py
rosrun image_sim retreive_image.py
rosrun image_sim tb3fetch_subscriber.py

For explanation of installing ROS and simulations read Jupyter notebook MSDS462Proj1.ipynb

For better understanding of final project working scripts read Jupyter notebook Chap462FinalNotebook.ipynb

June 13, 2020

Added Feasibility folder to contain work as part of the learning process
Moved image research to Feasibility/imagework
Moved publisher subscriber research to Feasibility/pubsubwork



