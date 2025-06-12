# MediaPipe Pose Estimator Node

This ROS 2 node uses **MediaPipe BlazePose** to extract full-body pose landmarks from camera images and publish them for downstream processing. It also provides a debug image stream and a service to toggle pose detection on or off.

---

## Functionality

- **Subscribes**: `/raw_image_out` (sensor_msgs/Image)
- **Publishes**:
  - `/pose/landmarks` (custom `PoseLandmarks` message)
  - `/pose/debug_image` (sensor_msgs/Image with landmark overlays)
  - `/pose/landmark` (not actively used)
- **Service**: `/enable_pose` – enable or disable pose detection

---

## Features

- Uses the `cv_bridge` package to convert ROS images to OpenCV.
- Computes 3D body landmark coordinates using MediaPipe BlazePose.
- Throttles publishing rate via the `publish_rate_hz` parameter.
- All parameters are declared for easy configuration and launch file integration.

---

## Parameters

**Note:** Despite the name, the `publish_rate_hz` parameter actually controls the **time interval in seconds** between published messages, not the frequency in Hz. This should be corrected....


| Name                      | Description                                 | Default  |
|---------------------------|---------------------------------------------|----------|
| `model_complexity`        | BlazePose model version (0–2)               | `1`      |
| `min_detection_confidence`| Minimum confidence to trigger detection     | `0.5`    |
| `min_tracking_confidence` | Minimum confidence to continue tracking     | `0.5`    |
| `enable_pose`             | Enable/disable processing                   | `True`   |
| `input_image_topic`       | Image topic to subscribe to                 | `/raw_image_out` |
| `pose_topic`              | Topic to publish full landmark arrays       | `/pose/landmarks` |
| `single_landmark_topic`   | Topic to publish one landmark (not used)    | `/pose/landmark` |
| `publish_rate_hz`         | Rate limit for publishing pose data         | `0.75`   |

---

## Notes

- This node is designed to interface with downstream components like an angle extractor and motion controller for the SAMI humanoid robot.
- Landmarks are published in world coordinates using MediaPipe's `pose_world_landmarks`.

---
##  License

BSD 3-Clause License

