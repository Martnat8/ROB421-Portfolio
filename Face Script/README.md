# LCD Robot Face – Blinking Eyes and Talking Mouth

This Python script uses **Pygame** to create an animated face for an LCD-screen-based robot. It features blinking eyes, shifting pupils, expressive eyebrows, and a lightly animated mouth to simulate idle "talking."

---

## Requirements

- Python 3
- [`pygame`](https://pypi.org/project/pygame/)

Install with:

```bash
pip install pygame
```

---

## How to Run

```bash
python Eye_Test2.py
```

The script creates a fullscreen-like window (480x800) without window borders, suitable for vertical LCD displays in robotics applications. It auto-hides the mouse and centers the eyes and mouth animation.

---

## Features

- **Blinking eyes** with smooth lid animation
- **Randomized pupil shifts** for natural eye movement
- **Animated eyebrows** above each eye
- **Mouth wiggling** in idle and simulated "talking" states
- Customizable timing for blinking, eye shifts, and mouth motion

---

## Context

Originally developed for a class project in which the robot SAMI displayed a face on an LCD screen. This animation acted as an idle or interactive face display to enhance user engagement.

---

## Notes

- Sound support is present but commented out.
- Designed for vertically mounted 480x800 displays.
