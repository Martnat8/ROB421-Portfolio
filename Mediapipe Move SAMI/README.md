# ROB 421 – SAMI Robot Motion Control Using MediaPipe

This project includes a set of ROS 2 packages used to control the SAMI robot based on pose data extracted using Google's MediaPipe framework.

---

## Dependencies

Make sure the following Python packages are installed in your environment:

- `mediapipe`
- `playsound`

You may also need to grant serial access permissions:

```bash
chmod 777 /dev/ttyUSB0
```

*(This may not be necessary depending on your system setup.)*

---

##  Angle Extraction

The angle extraction logic consists of two main functions:
- One computes the **acute angle between two vectors**.
- The other calculates the **angle between the normals of two planes**.

These are used to derive joint angles for SAMI’s servo motor positions based on pose landmarks.

---

##  How to Launch

1. Activate your MediaPipe virtual environment.
2. Navigate to your workspace:
    ```bash
    cd ~/your_workspace
    ```
3. Build and source:
    ```bash
    colcon build
    source install/setup.bash
    ```
4. Launch the system:
    ```bash
    ros2 launch camera_driver cameralaunch.py
    ros2 run move_sami move
    ```

---

##  Maintainer

Nathan Martin  
[martnat8@oregonstate.edu](mailto:martnat8@oregonstate.edu)

---

##  License

BSD 3-Clause License
