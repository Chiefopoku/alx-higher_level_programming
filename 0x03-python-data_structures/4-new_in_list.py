#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_new = my_list[:]
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        list_new[idx] = element
        return list_new
    return my_list
