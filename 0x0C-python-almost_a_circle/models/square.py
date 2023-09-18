#!/usr/bin/python3
""" a square module that is inherited from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """class square inherited from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """retrieving size"""
        return self.width

    @size.setter
    def size(self, value):
        """setting value to the size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """public method that assign attriutes to the method"""
        num_args = len(args)
        if num_args >= 1:
            self.id = args[0]
        if num_args >= 2:
            self.size = args[1]
        if num_args >= 3:
            self.x = args[2]
        if num_args >= 4:
            self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """a public method that returns the dictionary of class square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        """a string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
