# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 06:42:10 2021

@author : Princy Rasolonjatovo
@email  : princy.m.rasolonjatovo@gmail.com
@github : princy-rasolonjatovo
"""

from slide_shuffler import slide_shuffle
from slide import Slide
from solver import Solver, AStarSolver
from node import Node

if __name__ == '__main__':
    start = Slide(3, 3)
    goal = Slide(3, 3)
    slide_shuffle(start, move_count=50)
    solver = AStarSolver(Node(value=start), Node(value=goal))
    s = solver.solve()
    if s is not None:
        c = s
        while c.parent is not None:
            print(c.value)
            c = c.parent
    else:
        print('solution not found')

