def only_diff_elements(set_1, set_2):
    unique_elements = set()

    for element in set_1:
        if element not in set_2:
            unique_elements.add(element)

    for element in set_2:
        if element not in set_1:
            unique_elements.add(element)

    return unique_elements


set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
