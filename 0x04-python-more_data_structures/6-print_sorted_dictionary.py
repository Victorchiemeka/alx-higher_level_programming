#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for diction in a_dictionary:
        print(f"{diction}: {a_dictionary[diction]}")


a_dictionary = {"language": "C", "Number": 89, "track": "Low level", "ids": [1, 2, 3]}
print_sorted_dictionary(a_dictionary)
