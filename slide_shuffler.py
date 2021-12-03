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
    actions = [ choice(actions_list) for _ in range(move_count)]
    for action in actions:
        if action == Movement.UP:
            s.move_hole_up()
        elif action == Movement.DOWN:
            s.move_hole_down()
        elif action == Movement.RIGHT:
            s.move_hole_right()
        elif action == Movement.LEFT:
            s.move_hole_left()
        else:
            continue
        
    
