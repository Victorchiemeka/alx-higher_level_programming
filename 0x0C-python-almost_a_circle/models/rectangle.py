#!/usr/bin/python3
from base import Base


class Rectangle(Base):
    """A rectangle shape"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle object

        Args:
        width: the width of the rectangle
        height: the height of the rectangle
        x: the x-coordinate of the top-left of the rectangle
        y: the y-coordinate of the top-left of the rectangle
        id: the id of the rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("The width must be a non-negative integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("The height must be a non-negative integer.")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The x-coordinate of the top-left corner of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise TypeError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """The y-coordinate of the top-left corner of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer.")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """display the value of #"""
        for i in range(self.y):
            for i in range(self.x):
                print("#", end="")
            print()

    def __str__(self):
        """return format: [Rectangle] (<id>) <x>/<y> - <width>/<height>"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """assigns argument and key/value args to each attribute"""
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.width = args[1] if len(args) >= 2 else self.width
            self.height = args[2] if len(args) >= 3 else self.height
            self.x = args[3] if len(args) >= 4 else self.x
            self.y = args[4] if len(args) >= 5 else self.y
        else:
            for keys, val in kwargs.items():
                setattr(self, keys, val)
