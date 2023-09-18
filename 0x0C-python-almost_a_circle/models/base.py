#!/usr/bin/python3
""" a class Base module """

import json


class Base:
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """a static method that returns the json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """a class method that writes the json string of list_objs
        to a file
        """
        if list_objs is None:
            """if list is none save empty list"""
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            j = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(j)

    @staticmethod
    def from_json_string(json_string):
        """a method that returns the list of json string representation"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """method that returns instance with all attribute already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        if cls.__name__ == "Square":
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """a class method that returns the list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dict_list = json.loads(json_string)
                return [cls.create(**dictionary) for dictionary in dict_list]
        except FileNotFoundError:
            return []
