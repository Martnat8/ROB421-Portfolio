# Camera Driver

This package contains a node that publishes image frames from a UVC compliant camera

camera_driver.py
_____________________________________________________________________________________

## camera_driver

The `camera_driver` node captures video frames from a UVC-compliant USB camera and publishes them as `sensor_msgs/Image` on the `/raw_image_out` topic. By default it uses:

- device_id: `0` (e.g. `/dev/video0`)  
- fps: `15.0` (frames per second)  
- frame_width: `1280` (pixels)  
- frame_height: `720` (pixels)  
- encoding: `bgr8` (OpenCV’s BGR8 format)  
- frame_id: `camera` (the ROS TF frame stamped on each image)

These parameters can all be changed in the launch file.

To start the camera stream compile and run:

ros2 launch camera_driver cameralaunch.py

_____________________________________________________________________________________
Maintainer - Nathan Martin - martnat8@oregonstate.edu
_____________________________________________________________________________________
License - BSD 3-Clause

