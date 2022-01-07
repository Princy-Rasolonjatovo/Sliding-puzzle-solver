# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 06:42:10 2021

@author : Princy Rasolonjatovo
@email  : princy.m.rasolonjatovo@gmail.com
@github : princy-rasolonjatovo
"""

from slide_shuffler import slide_shuffle
from slide import Slide
from solver import AStarSolver
from node import Node

if __name__ == '__main__':
    start = Slide(2, 3)
    goal = Slide(2, 3)
    # ! WARNING: this is a test
    goal.move_hole_up()
    print(goal)
    # ! ENDWARNING
    # slide_shuffle(start, move_count=20)
    # solver = AStarSolver(Node(value=start), Node(value=goal))
    # print('puzzle: ')
    # print(start)
    # print()
    # print('solving puzzle ...')
    # s = solver.solve()
    # if s is not None:
    #     c = s
    #     while c.parent is not None:
    #         print(c.value)
    #         c = c.parent
    # else:
    #     print('solution not found')

