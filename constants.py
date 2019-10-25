#!/usr/bin/env python3

# Created by: Amir Mersad
# Created on: Sep 2019
# This constants file is for Space Alien gamepad

# CiruitPython screen is 160x120 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 120
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
FPS = 60
SPRITE_MOVEMENT_SPEED = 1

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released"
}