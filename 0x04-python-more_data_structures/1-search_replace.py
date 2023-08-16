#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace


my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
search_replace(my_list, 2, 89)

print(my_list)  # Output: [1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
