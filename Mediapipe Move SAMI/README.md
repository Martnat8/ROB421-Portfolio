# ROB 421 SAMI Robot Motion Control Using MediPipe

This package contains a variety of packages that ammount to moving SAMI
based on Google's Mediapipe.

Youll need to install:

Mediapipe
playsound

You may need to run this command: (don't think this is needed rn)

chmod 777 /dev/ttyUSB0
_____________________________________________________________________________________

The math for the angle extractor has two functions. One takes the acute angle between
two vectors, the other finds the angle between the normals of two planes. These account
for the angles of all of the arm joint servo motor positions. 
_____________________________________________________________________________________
launch into mediapipe virtual environment
cd ~/<package workspace>
colcon build 
source install/setup.bash
ros2 launch camera_driver cameralaunch.py
ros2 run move_sami move

_____________________________________________________________________________________
_____________________________________________________________________________________
Maintainer - Nathan Martin - martnat8@oregonstate.edu
_____________________________________________________________________________________
License - BSD 3-Clause
_____________________________________________________________________________________


