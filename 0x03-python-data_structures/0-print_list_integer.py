#!/usr/bin/python3
def print_list_integer(my_list=None):
    if my_list is None:
        my_list = []  # Create a new list if None is passed

    for i in my_list:
        print("{}".format(i))
