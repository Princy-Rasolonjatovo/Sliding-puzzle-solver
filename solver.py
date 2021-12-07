
from __future__ import annotations
from typing import List, Tuple, Any, Set
from queue import PriorityQueue
from slide import Slide
from node import Node

class SlideNode(Node, Slide):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.value = super()._mat

    def __hash__(self):
        return super().__hash__()

    def __eq__(self, o: Node | SlideNode):
        return hash(self) == hash(o)

    def childrens(self)-> List[SlideNode]:
        vup = self.copy()
        vdown = self.copy()
        vleft = self.copy()
        vright = self.copy()
        return filter(lambda canmove, value: canmove, [
            (vup.move_hole_up(), vup),
            (vdown.move_hole_down(), vdown),
            (vleft.move_hole_left(), vleft),
            (vright.move_hole_right(), vright)
        ])

        
        

# WARNING: does not work yet
class Solver:
    def __init__(self, source: Node):
        assert isinstance(source, Node), '[BadArgumentError] source type: {0} expected: {1}'.format(type(source), type(Node))
        self.source: Node = source  #Source Node
        self._solvedTile = None
        self._visiteds: List[Node] = []
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
    def __init__(self, start: Node, goal: Node, *args, **kwargs):
        self.start: Node = start
        self.goal: Node = goal

    def __heuristic(self):
        pass

    def __g(self):
        pass

    def __astar(self):
        toVisit: PriorityQueue[Node] = PriorityQueue()
        visited: Set[Node] = set()

        toVisit.put(self.start)
        while not toVisit.empty():
            current = toVisit.get()
            


    def solve(self):
        pass