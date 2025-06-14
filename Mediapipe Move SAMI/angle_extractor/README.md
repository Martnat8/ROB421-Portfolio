# Angle Processing for SAMI Robot

This folder contains two ROS2 nodes used to process pose data into servo commands for the SAMI humanoid robot.

---

## Files

### `angleextractor.py`
- Subscribes to: `/pose/landmarks` (custom `PoseLandmarks` message)
- Publishes: `/joint_angles` (JSON-formatted `std_msgs/String`)
- Function: Computes joint angles from MediaPipe landmarks using vector geometry. Calculates elbow, shoulder, bicep, and chest joint angles.

### `anglecorrector.py`
- Subscribes to: `/joint_angles`
- Publishes: `/joint_angles_corrected`
- Function: Translates raw joint angles into servo-compatible values using a calibrated mapping (servo home, direction, limits) defined per joint. Clamps values to mechanical limits.

## Adding New Joints

To support additional joints in the correction pipeline (`anglecorrector.py`):

1. **Update `self.joint_info`**:
   Add an entry for the new joint in the following format:
   ```python
   "NewJointName": {
       "servohome": <int>,      # Servo angle value at home
       "min": <int>,            # Minimum servo angle limit
       "max": <int>,            # Maximum servo angle limit
       "direction": <1 or -1>,  # Based on direction of CCW or CW in SAMI's joint servo frame
       "home_angle": <int>      # World-space angle corresponding to servohome
   }
   ```

2. **Ensure the joint is published by `angleextractor.py`**:
   If the new joint requires angle computation, add logic in `angleextractor.py` using `compute_angle()` or `compute_rotation()`.

3. **Test**:
   Run both nodes and verify the new joint appears in `/joint_angles_corrected`.
---

## Purpose

Together, these nodes convert raw pose landmarks into robot-ready joint commands, bridging the gap between camera-based human motion and servo-actuated mimicry in SAMI.

> These files are intended to be used as part of a larger ROS2 system involving a MediaPipe-based pose estimator and SAMI's servo control logic.

---

## Notes

This was developed with a very cheap UVC camera, Mediapipe did it's best to find some 3 dimensional positioning, but it was never very accurate. SAMI mirrors pretty effectively if you keep your motions restricted to the plane of your body, but if you stick your arms forward or back things get a little weird. Future endeavors could integrate some depth measurements to help with this.
