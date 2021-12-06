#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:17:09 2021

@author: P.Rasolonjatovo
@e-mail: princy.m.rasolonjatovo@gmail.com
"""
from __future__ import annotations
from copy import deepcopy, copy
from typing import List, Any, Callable


class _List(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setitemCallback: Callable[[int, type, int], None] = kwargs.get('setitemCallback')
        self._last_index = kwargs.get('last_index')
    
    def __getitem__(self, index):
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        if self.setitemCallback is not None:
            self.setitemCallback(index, value, self._last_index)
        return super().__setitem__(index, value)


class Slide:
    def __init__(self, lines: int, cols: int, hole_pos: tuple | None= None, **kwargs):
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
        self._mat = []
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
        __repr = """"""
        for i in range(self._lines * self._cols):
            if i % self._cols == 0:
                __repr += '\n'
            __repr += '%3d' % (self._mat[i])
        return __repr
        
     
    def __eq__(self, o: Slide) -> bool:
        if isinstance(o, Slide):
            return self.mat == o.mat and self.lines == o.lines and self.cols == o.cols
        return False
    
    def __build_mat(self):
        self._mat = [i + 1 for i in range(self._lines * self._cols)]
        if self._hole_pos is None:
            self._mat[self._lines * self._cols - 1] = 0
            self._hole_pos = (self._lines - 1, self._cols - 1)
        else:
            i, j = self._hole_pos
            self._mat[i + j * self._cols] = 0

    def copy(self) -> Slide:
        return deepcopy(self)

    def __freeze_mat(self):
        if not self._hasfreezed:
            self._mat = tuple(self._mat)
            self._hasfreezed = True
    
    def freeze(self):
        self.__freeze_mat()
        
    def set_tile(self, pos: tuple, val: int):
        assert not self._hasfreezed,"[TileHasFreezedError] The mat is immutable"
        i, j = pos
        assert i < self.lines and j < self.cols and i >= 0 and i >= 0, "[BadIndex] i:{0}, j{1}".format(i, j)
        self[i][j] = val

    def __getitem__(self, index: int):
        if index < 0 or index >= self._lines:
            raise IndexError(f'index {index} off-limits, matrix size({self._lines}, {self._cols})')
        return _List(self._mat[index * self.lines: index * self.lines + self._cols], setitemCallback=self.__get_col_guard_callback, last_index=index)

    def __setitem__(self, i: int, value: list[int]):
        # check dimension
        if isinstance(value, (list, tuple)):
            if len(value) == self._cols:
                for j, v in enumerate(value):
                    self._mat[i + 1 + j] = v
            else:
                raise Exception(f'[DimensionError] cannot assign object of dimension {len(value)} into {self._cols} dim')
        else:
            raise TypeError(f'Cannot assign type {type(value)}')
        print(f'i: {i} val: {value}')

    def __get_col_guard_callback(self, index: int, value: type, last_index: int):
        # check if index is int (col)
        if isinstance(index, int):
            # assign to the value in self._mat at coordinates(last_index, index) object[last_index][index] = value
            self._mat[self._cols * last_index + index] = value
        else:
            raise Exception('[BadIndex]')

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
        t1_val = self[t1_i][t1_j]
        self[t1_i][t1_j] = self[t2_i][t2_j]
        self[t2_i][t2_j] = t1_val
    
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
        if hi + 1 < self.lines:
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
        if hj + 1 < self.cols:
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
        if hj - 1 >= 0:
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
        return hash(tuple(self._mat))
    
    def get_movements(self) -> list[Slide]:
        """
            Get possible Tile conformations on one move
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
     