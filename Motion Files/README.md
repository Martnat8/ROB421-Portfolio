# ROB 421 – BAJAN Team Motion Files for SAMI

This folder contains motion files created by Team BAJAN for **ROB 421: Applied Robotics** at Oregon State University. 
Each file is written in `.json` format and defines a sequence of **keyframes** used to control the servo motor positions 
of the [SAMI Robot](https://github.com/jlruballos/sami_ws).

---

## File Structure

Each motion file includes:
- A `Name` field describing the motion 
- A list of `Keyframes`, where each keyframe defines:
  - `HasJoints`, `HasAudio`, and `HasEmote` flags
  - An optional `AudioClip` and `Expression`
  - `WaitTime` (milliseconds to pause after the frame)
  - `JointMoveTime` (how long to move to this pose)
  - A list of `JointAngles`, each with:
    - `Joint`: the name of the joint
    - `Angle`: the target angle for the joint

These files are parsed by SAMI's motion controller to execute expressive, timed robotic gestures.

---

## 📄 License

BSD 3-Clause License
