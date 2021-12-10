
from typing import List
from slide import Slide
from node import Node
from math import dist
from queue import PriorityQueue
from multiprocessing import Process, cpu_count, Pipe, Pool


class AStarSolver:
    def __init__(self, start: Node, goal: Node):
        self.start: Node = start
        self.goal: Node = goal
        self.path: Node = start

    def __heuristic(self, node: Node):
        return dist(node.value.mat, self.goal.value.mat)

    def solve(self) -> Node:
        closedList: set = set()
        openList: PriorityQueue = PriorityQueue()
        openList.put(self.start)
        while not openList.empty():
            current = openList.get()
            if current == self.goal:
                return current
            closedList.add(current)
            for s in current.childrens():
                s = Node(value=s)
                if s not in closedList:
                    s.parent = current
                    s.h = self.__heuristic(s)
                    s.g += 1
                    openList.put(s)
        return None
            
        
