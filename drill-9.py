"""Drill 9: 방향키 이동과 네 action 애니메이션."""

import math
import os
from pathlib import Path
from time import perf_counter

from pico2d import *

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024

FRAME_WIDTH = 100
FRAME_HEIGHT = 100
FRAME_COUNT = 8

MOVE_SPEED = 250.0
IDLE_FPS = 8.0
RUN_FPS = 12.0

IDLE_RIGHT = "idle_right"
IDLE_LEFT = "idle_left"
RUN_RIGHT = "run_right"
RUN_LEFT = "run_left"

# clip_draw는 이미지의 아래쪽을 y 좌표 원점으로 사용한다.
ACTIONS = {
    IDLE_RIGHT: (300, IDLE_FPS),
    IDLE_LEFT: (200, IDLE_FPS),
    RUN_RIGHT: (100, RUN_FPS),
    RUN_LEFT: (0, RUN_FPS),
}

class Boy:
    def __init__(self, image):
        self.image = image
        self.x = CANVAS_WIDTH / 2
        self.y = CANVAS_HEIGHT / 2
        self.facing = 1
        self.action = IDLE_RIGHT
        self.frame = 0.0

    def change_action(self, action):
        if self.action != action:
            self.action = action
            self.frame = 0.0

    def update(self, pressed_keys, dt):
        dx = int(SDLK_RIGHT in pressed_keys) - int(SDLK_LEFT in pressed_keys)
        dy = int(SDLK_UP in pressed_keys) - int(SDLK_DOWN in pressed_keys)

        if dx != 0:
            self.facing = dx

        if dx != 0 or dy != 0:
            action = RUN_RIGHT if self.facing == 1 else RUN_LEFT
        else:
            action = IDLE_RIGHT if self.facing == 1 else IDLE_LEFT
        self.change_action(action)

        distance = math.hypot(dx, dy)
        if distance != 0:
            self.x += dx / distance * MOVE_SPEED * dt
            self.y += dy / distance * MOVE_SPEED * dt

        half_width = FRAME_WIDTH / 2
        half_height = FRAME_HEIGHT / 2
        self.x = max(half_width, min(CANVAS_WIDTH - half_width, self.x))
        self.y = max(half_height, min(CANVAS_HEIGHT - half_height, self.y))

        row, fps = ACTIONS[self.action]
        self.frame = (self.frame + fps * dt) % FRAME_COUNT

    def draw(self):
        row, fps = ACTIONS[self.action]
        self.image.clip_draw(
            int(self.frame) * FRAME_WIDTH, row,
            FRAME_WIDTH, FRAME_HEIGHT, self.x, self.y
        )

def handle_events(pressed_keys):
    running = True
    arrow_keys = (SDLK_LEFT, SDLK_RIGHT, SDLK_UP, SDLK_DOWN)
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key in arrow_keys:
                pressed_keys.add(event.key)
        elif event.type == SDL_KEYUP and event.key in arrow_keys:
            pressed_keys.discard(event.key)
    return running

def main():
    previous_directory = Path.cwd()
    os.chdir(Path(__file__).resolve().parent)
    try:
        open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
        try:
            background = load_image("TUK_GROUND.png")
            boy = Boy(load_image("animation_sheet.png"))
