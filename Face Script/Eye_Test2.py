#!/usr/bin/env python3
# Eye_Test2.py
import os
import pygame
import sys
import math
import random

# Set position (optional, in case you need to target a specific screen)
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

# Initialize
pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((480, 800), pygame.NOFRAME)

pygame.mouse.set_pos((800, 480))
pygame.display.set_caption("Blinking Eyes")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Eye positions and dimensions (rotated 90°, so vertical rectangles)
eye_width = 80
eye_height_max = 200
left_eye_base = [120, 100]  # base x, y
right_eye_base = [310, 100]
left_eye_pos = left_eye_base[:]
right_eye_pos = right_eye_base[:]

# Eyebrow dimensions (wider and more offset)
eyebrow_width = 100
eyebrow_height = 10
eyebrow_offset = 40

# Mouth position and dimensions
mouth_pos = [220, 550]  # x, y
mouth_width = 140
mouth_height_base = 20
mouth_amplitude = 5  # How much the mouth "wiggles"
mouth_freq = 0.5     # Slower wiggle (Hz)
mouth_height = mouth_height_base
next_mouth_shift_time = 0
mouth_shift_interval_range = (2000, 5000)  # ms

# Talk animation
talking = False
talk_start_time = 0
talk_duration = 1000  # ms
next_talk_time = 0
talk_interval_range = (4000, 9000)  # ms

# Blink animation settings
blink_interval = 3000      # Time between blinks (ms)
blink_duration = 600       # Total blink cycle time (ms)
blink_progress = 0         # Progress through blink cycle (0–1)
blinking = False
blink_start_time = 0

# Eye movement settings
eye_movement_timer = 0
next_eye_shift_time = 0
eye_shift_interval_range = (3000, 6000)  # in ms
eye_shift_x = 0
eye_shift_y = 0
max_eye_shift = 20  # pixels

# Main loop
running = True
while running:
    now = pygame.time.get_ticks()
    screen.fill(WHITE)

    # Start blinking if time
    if not blinking and now - blink_start_time > blink_interval:
        blinking = True
        blink_start_time = now

    # Animate blink
    if blinking:
        elapsed = now - blink_start_time
        half = blink_duration // 2
        if elapsed < blink_duration:
            if elapsed < half:
                blink_progress = elapsed / half
            else:
                blink_progress = 1 - ((elapsed - half) / half)
        else:
            blinking = False
            blink_progress = 0

    # Animate small random eye movement (x and y)
    if now > next_eye_shift_time:
        if random.random() < 0.5:
            eye_shift_x = random.randint(-max_eye_shift, max_eye_shift)
            eye_shift_y = random.randint(-max_eye_shift, max_eye_shift)
        else:
            eye_shift_x = 0
            eye_shift_y = 0
        next_eye_shift_time = now + random.randint(*eye_shift_interval_range)

    # Update eye positions
    left_eye_pos[0] = left_eye_base[0] + eye_shift_x
    left_eye_pos[1] = left_eye_base[1] + eye_shift_y
    right_eye_pos[0] = right_eye_base[0] + eye_shift_x
    right_eye_pos[1] = right_eye_base[1] + eye_shift_y

    # Compute eye height for two eyelids
    lid_height = eye_height_max * 0.5 * blink_progress
    eye_visible_height = eye_height_max - 2 * lid_height

    # Draw eyes with rounded corners
    pygame.draw.rect(screen, BLACK, (left_eye_pos[0], left_eye_pos[1] + lid_height, eye_width, eye_visible_height), border_radius=20)
    pygame.draw.rect(screen, BLACK, (right_eye_pos[0], right_eye_pos[1] + lid_height, eye_width, eye_visible_height), border_radius=20)

    # Draw eyebrows above the eyes (centered and offset)
    pygame.draw.rect(screen, BLACK, (left_eye_pos[0] - (eyebrow_width - eye_width) // 2, left_eye_pos[1] - eyebrow_offset, eyebrow_width, eyebrow_height))
    pygame.draw.rect(screen, BLACK, (right_eye_pos[0] - (eyebrow_width - eye_width) // 2, right_eye_pos[1] - eyebrow_offset, eyebrow_width, eyebrow_height))

    # Animate mouth height using sine wave + random variation or talking
    if talking:
        mouth_height = mouth_height_base + 20 * math.sin(10 * now / 100.0)
        if now - talk_start_time > talk_duration:
            talking = False
            next_talk_time = now + random.randint(*talk_interval_range)
    else:
        mouth_time = now / 1000.0
        base_mouth_height = mouth_height_base + mouth_amplitude * math.sin(2 * math.pi * mouth_freq * mouth_time)
        if now > next_mouth_shift_time:
            if random.random() < 0.5:
                mouth_height = base_mouth_height + random.uniform(-3, 3)
            else:
                mouth_height = base_mouth_height
            next_mouth_shift_time = now + random.randint(*mouth_shift_interval_range)

        if now > next_talk_time:
            talking = True
            talk_start_time = now
            # pop_sound.play()  # sound removed

    # Draw the mouth as a rounded rectangle with animated height
    pygame.draw.rect(screen, BLACK, (mouth_pos[0], mouth_pos[1], mouth_width, mouth_height), border_radius=20)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
