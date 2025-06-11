# SAMI Robot – Head and Screen Mount CAD Files

This folder contains Fusion 360 and STL files used to prototype parts for the SAMI Robot's head and screen mounting system. These parts are designed to work with the [SAMI Robot project](https://github.com/jlruballos/sami_ws).

---

## Components Included

- **Screen Bracket**  
  Holds the LCD screen securely in place.

- **Head Cover**  
  Enclosure piece designed to mount over the face frame and protect internal components.

- **Ear (Speaker) Brackets**  
  Designed to attach audio output modules to either side of the head.

- **Backplate / Neck Bracket**  
  Supports and stabilizes the connection between the robot's neck and head.

---

##  Files in This Folder

- `SAMIHead1.png`, `SAMIHead2.png`, `SAMIHead3.png` – preview renders of the head assembly
- `ear_bracket v2.f3d` – Fusion 360 file for speaker/ear mount
- `head_cover v27.f3d` – Fusion 360 file for top cover
- `new_Backplate v28.f3d` – Fusion 360 file for back plate and neck support
- `headUpdate_Sami.v2 v1.stl` – export-ready STL of a head assembly variant

---

##  Compatible Display

Designed to fit the following LCD screen (portrait orientation):

[HMTECH 7" 800×480 LCD with Speakers (Amazon)](https://www.amazon.com/HMTECH-Raspberry-800x480-Dual-Speaker-Non-Touch/dp/B0C6963887?th=1)

---

##  Notes for Future Use

The current design assumes a **vertical screen orientation**, but this caused stability issues with SAMI’s torso and neck motors. If you plan to replicate or modify this build, we recommend:

- Re-orienting the screen for **landscape mode**, _or_
- Reinforcing the **servo motors** for torso tilt, bow, and neck movement

---

## 📄 License

BSD 3-Clause License
