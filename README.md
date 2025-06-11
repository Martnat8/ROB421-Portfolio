# ROB 421 – BAJAN Robotics Team Term Project

This repository contains the final project for the **BAJAN Robotics team** in **ROB 421: Applied Robotics** at Oregon State University. The project centers around SAMI, a servo-actuated humanoid robot capable of interpreting human pose using MediaPipe and responding with expressive movements and animations.

---

##  Folder Overview

### `CAD Files/`
Includes all Fusion 360 (`.f3d`) and STL (`.stl`) files for the **robot head and screen mounting system**. These parts were designed to fit a specific vertical LCD and include mounts for speakers, neck stabilization, and more.

### `Face Script/`
A standalone **Pygame-based animation script** that simulates SAMI’s facial expressions on an LCD screen. It includes animated blinking eyes, shifting pupils, and a talking mouth effect designed to run as a full-screen overlay.

### `Mediapipe Move SAMI/`
Contains all source files related to:
- MediaPipe-based **vector landmark extraction**
- **Camera drivers** for live pose tracking
- **Servo movement execution** for SAMI

This folder also includes its own detailed `README.md` that explains setup, launch instructions, and system architecture.

### `Motion Files/`
Contains all robot **motion sequences** in `.json` format. Each file defines a series of keyframes that control SAMI's servo positions, timing, and optional audio/emotion metadata. These are parsed by the SAMI robot’s runtime to execute expressive, timed motions.


---

##  Project Demo

Check out our robot in action on Instagram:  
👉 [@rob421_sami5](https://www.instagram.com/rob421_sami5/)

---

## 📄 License

BSD 3-Clause License
