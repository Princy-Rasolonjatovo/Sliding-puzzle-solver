
from slide import Slide
from node import Node
from math import dist
from queue import PriorityQueue


# WARNING: does not work yet
class Solver:
    def __init__(self, source: Node):
        assert isinstance(source, Node), '[BadArgumentError] source type: {0} expected: {1}'.format(type(source), type(Node))
        self.source = source  #Source Node
        self._solvedTile = None
        self._visiteds = []
    def __build_graph(self):
        pass
    
    def __dfs(self, src: Node) -> bool:
        print(src.value)
        if self.issolved(src.value):
            return True
        for child in src.value.get_movements():
            cNode:Node = Node(value=child, parent=src)
            valHash = hash(src.value)
            if valHash in self._visiteds:
                continue
            else:
                self._visiteds.append(valHash)
            return self.__dfs(cNode)
        # return False
    
    def solve(self) -> None:
        solved: bool = self.__dfs(self.source)
        print(f"the solution has{'' if solved else ' not'} been found")
    
    def issolved(self, slide: Slide) -> bool:
        if self._solvedTile is None:
            self._solvedTile = Slide(slide.lines, 
                           slide.cols, 
                           hole_pos=(slide.lines-1, slide.cols-1))
        return self._solvedTile == slide


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