#!/usr/bin/python3
from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width
