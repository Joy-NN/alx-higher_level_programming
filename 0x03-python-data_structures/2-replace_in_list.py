#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list
original_list = [1, 2, 3, 4, 5]
new_list = replace_in_list(original_list, 2, 99)
print(new_list)

new_list = replace_in_list(original_list, -1, 99)
print(new_list)


new_list = replace_in_list(original_list, 10, 99)
print(new_list)
