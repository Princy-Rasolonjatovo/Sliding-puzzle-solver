#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:17:09 2021

@author: P.Rasolonjatovo
@e-mail: princy.m.rasolonjatovo@gmail.com
"""
from __future__ import annotations
from copy import deepcopy
from typing import List, Any, Callable



class Slide:
    def __init__(self, lines: int=3, cols: int=3, hole_pos: tuple=(2,2), **kwargs):
        """
        Represent a SliddingPuzzle state

        Parameters
        ----------
        lines : mat.n
            DESCRIPTION.
        cols : mat.m
            DESCRIPTION.
        hole_pos : tuple<int, int> 
            by default pos<lines-1, cols-1>

        Returns
        -------
        None.

        """
        self._lines = lines
        self._cols = cols
        
        self._mat = [[0 for c in range(cols)] for _ in range(lines)]
        self._hole_pos = hole_pos
        self._hasfreezed = False # self._mat has been freezed?
        
        self.__build_mat()
    
    @property
    def mat(self):
        return self._mat
    
    @property
    def lines(self):
        return self._lines
    
    @property
    def cols(self):
        return self._cols
    
    @property
    def hole_pos(self):
        return self._hole_pos
    
    def __repr__(self):
        _s = ""
        for i in range(self.lines):
            _s += repr(self._mat[i])
            _s += '\n'
        return "Slide<\n{0}>\n".format(_s)
     
    def __eq__(self, o: Slide) -> bool:
        if isinstance(o, Slide):
            return self.mat == o.mat and self.lines == o.lines and self.cols == o.cols
        return False
    
    def __build_mat(self):
        n = 1
        hi, hj = self._hole_pos 
        for i in range(self.lines):
            for j in range(self.cols):
                if (i, j) != (hi, hj):
                    self._mat[i][j] = n
                    n += 1
                    
    def __freeze_mat(self):
        if not self._hasfreezed:
            self._mat = tuple(map(tuple, self._mat))
            self._hasfreezed = True
    
    def freeze(self):
        self.__freeze_mat()
        
    def set_tile(self, pos: tuple, val: int):
        assert not self._hasfreezed,"[TileHasFreezedError] The mat is immutable"
        i, j = pos
        assert i < self.lines and j < self.cols and i >= 0 and i >= 0, "[BadIndex] i:{0}, j{1}".format(i, j)
        self._mat[i][j] = val
    
    def move_hole(self, pos: tuple) -> list:
        """
        Constraint<BoardBoundaries>
        
        Move the hole of the slidding puzzle to a new position

        Parameters
        ----------
        pos : tuple<int, int>
            Coordinates of the new location.

        Returns
        -------
        None.

        """
        i, j = pos
        hi, hj = self._hole_pos
        # Check board boundaries
        # assert hi == i-1 or hi == i+1, "[OutOfBoundariesError] i: {0}, j: {1}".format(i, j)
    
    def __swap_tiles(self, t1: tuple, t2: tuple):
        t1_i, t1_j = t1
        t2_i, t2_j = t2
        t1_val = self._mat[t1_i][t1_j]
        t2_val = self._mat[t2_i][t2_j]
        self._mat[t1_i][t1_j] = t2_val
        self._mat[t2_i][t2_j] = t1_val
    
    def move_hole_up(self) -> bool:
        assert not self._hasfreezed, "[TileHasFreezedError] The mat is immutable"
        hi, hj = self._hole_pos
        i, j = -1, -1
        if hi-1 >= 0:
            i = hi
            j = hj
            hi -= 1
            self._hole_pos = (hi, hj)
            self.__swap_tiles(self._hole_pos, (i, j))
            return True
        return False

    def move_hole_down(self) -> bool:
        assert not self._hasfreezed, "[TileHasFreezedError] The mat is immutable"
        hi, hj = self._hole_pos
        i, j = -1, -1
        if hi+1 < self.lines:
            i = hi
            j = hj
            hi += 1
            self._hole_pos = (hi, hj)
            self.__swap_tiles(self._hole_pos, (i, j))
            return True
        return False
    
    def move_hole_right(self) -> bool:
        assert not self._hasfreezed, "[TileHasFreezedError] The mat is immutable"
        hi, hj = self._hole_pos
        i, j = -1, -1
        if hj+1 < self.cols:
            i = hi
            j = hj
            hj += 1
            self._hole_pos = (hi, hj)
            self.__swap_tiles(self._hole_pos, (i, j))
            return True
        return False
    
    def move_hole_left(self) -> bool:
        assert not self._hasfreezed, "[TileHasFreezedError] The mat is immutable"
        hi, hj = self._hole_pos
        i, j = -1, -1
        if hj-1 >= 0:
            i = hi
            j = hj
            hj -= 1
            self._hole_pos = (hi, hj)
            self.__swap_tiles(self._hole_pos, (i, j))
            return True
        return False
    
    def copy(self):
        return deepcopy(self)
    
    def __hash__(self):
        return hash(tuple(map(tuple, self._mat)))
    
    def get_movements(self) -> list[Slide]:
        """
            Get possible Tile conformation on one move
        Returns
        -------
        list<Slide>
            DESCRIPTION.

        """
        slides = []
        if self.move_hole_left():
            slides.append(self.copy())
            self.move_hole_right()
        if self.move_hole_right():
            slides.append(self.copy())
            self.move_hole_left()
        if self.move_hole_up():
            slides.append(self.copy())
            self.move_hole_down()
        if self.move_hole_down():
            slides.append(self.copy())
            self.move_hole_up()
        return slides
# Test
s = Slide()
s.move_hole_up()
        
        