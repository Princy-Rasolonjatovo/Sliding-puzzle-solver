# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 06:42:10 2021

@author : Princy Rasolonjatovo
@email  : princy.m.rasolonjatovo@gmail.com
@github : princy-rasolonjatovo
"""

from slide_shuffler import slide_shuffle
from slide import Slide
from solver import Solver
from node import Node

if __name__ == '__main__':
    slide = Slide()
    slide_shuffle(slide, move_count=45)
    solver = Solver(Node(value=slide, parent=None))
    solver.solve()
    #print(slide)
