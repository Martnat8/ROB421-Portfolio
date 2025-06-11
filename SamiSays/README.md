# SAMI Says – Prototype Game with Mediapipe Integration

This folder contains prototype ROS 2 nodes for a "SAMI Says" game designed for the SAMI robot, developed by Team BAJAN for the ROB 421 course at Oregon State University.

---

## Concept

The idea was to create an interactive pose-matching game where SAMI performs a random pose and waits for the user to mirror it in front of a webcam. 
The system uses **MediaPipe** to extract human joint angles and compares them to SAMI’s predefined poses. If the match is close enough, SAMI celebrates
and moves on to the next pose.

---

## Components

- `sami_says.py`: Selects a random target pose, publishes it to SAMI, and listens for pose matches based on joint angle data.
- `fake_angle.py`: Publishes a hardcoded pose on a topic to simulate or test the system without MediaPipe input.

---

##  Limitations & Status

- **Not fully integrated**: The game was not fully hooked up to live MediaPipe data during development.
- **Unverified behavior**: Final pose-matching logic was not tested end-to-end.
- **Standalone**: These nodes were never fully run and may require manual startup and topic remapping.
- **Visualization and feedback** to the user were not implemented.

---

## Future Work Ideas

- Connect to live joint angles from MediaPipe (via angle_extractor).
- Add visual or audio feedback when poses are matched or failed.
- Develop a score system or timed rounds to make it more game-like.

---
---

##  License

BSD 3-Clause License
