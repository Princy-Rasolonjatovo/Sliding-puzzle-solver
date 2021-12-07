#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 12:34:13 2021

@author: P.Rasolonjatovo
@e-mail: princy.m.rasolonjatovo@gmail.com
"""
from __future__ import annotations
from slide import Slide
from typing import List


class Node:
    def __init__(self, value: Slide, parent: Node= None):
        self.value:Slide = value
        self.parent:Node = parent
        self.visited:bool = False
        self.g = 0
        self.h = 0
    
    @property
    def d(self) -> float:
        return self.g + self.h
    
    def walk(self):
        pass

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other: Node) -> bool:
        return hash(self.value) == hash(other.value)

    def __lt__(self, other: Node) -> bool:
        return self.d < other.d

    def __gt__(self, other: Node):
        return self.d > other.d

    def childrens(self) -> List[Slide]:
        return self.value.get_movements()
