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
