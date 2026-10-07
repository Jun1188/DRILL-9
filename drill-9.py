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
