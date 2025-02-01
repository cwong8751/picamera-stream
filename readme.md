# picamera-stream 


## what is this
ros node for publishing raspberry pi camera stream 


## structure
<code>old</code> is old code, doesn't work anymore. 

<code>camera_stream</code> is the folder you want. 


## how to run
1. download the <code>camera_stream</code> folder and put it in the pi
2. use <code>source install/setup.bash</code> and source the ros2 workspace 
3. use <code>ros2 run cam_stream camera_publisher</code> to run the node

## build 
1. cd to <code>cd ~/camera-stream/cam_stream_ws</code>
2. build via <code>colcon build --packages-select cam_stream</code>
3. source installation file via <code>source install/setup.bash</code>


## troubleshooting
check for permissions: 

<code>chmod +x src/cam_stream/cam_stream/camera_publisher.py</code>


list all active topics, check for something related to camera and image_raw
<code>ros2 topic list</code>

## how to view image
1. rviz - it doens't work
2. ros-image-view



## assumptions
1. you have ros2 installed
2. your ros2 works fine
3. dependencies are all installed



written by carl, jan 18 2025. 
