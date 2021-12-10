#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 15:25:19 2021

@author: P.Rasolonjatovo
@e-mail: princy.m.rasolonjatovo@gmail.com
"""
from __future__ import annotations
from slide import Slide
from random import choice
from enum import unique, Enum
from typing import List


@unique
class Movement(Enum):
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4


def slide_shuffle(s: Slide, move_count=30):
    actions_list: List[Movement] = [
        Movement.UP,
        Movement.DOWN,
        Movement.RIGHT,
        Movement.LEFT    
    ]
    while move_count > 0:
        action = choice(actions_list)
        if action == Movement.UP:
            if s.move_hole_up():
                move_count -= 1
        elif action == Movement.DOWN:
            if s.move_hole_down():
                move_count -= 1
        elif action == Movement.RIGHT:
            if s.move_hole_right():
                move_count -= 1
        elif action == Movement.LEFT:
            if s.move_hole_left():
                move_count -= 1
        else:
            continue
        
    
