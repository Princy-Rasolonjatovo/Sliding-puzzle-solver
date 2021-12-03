#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 12:34:13 2021

@author: P.Rasolonjatovo
@e-mail: princy.m.rasolonjatovo@gmail.com
"""
from __future__ import annotations
from slide import Slide

class Node:
    def __init__(self, value: Slide, parent: Node= None):
        self.value:Slide = value
        self.parent:Node = parent
        self.visited:bool = False
        
    def walk(self):
        pass
    
    def __eq__(self, o: Node) -> bool:
        return (
            self.state == o.state and 
            self.slide == o.slide and
            self.parent == o.parent)

