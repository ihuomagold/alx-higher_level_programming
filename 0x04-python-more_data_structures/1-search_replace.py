#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list =[]
    my_list = list(map(lambda x: x.replace(search, replace), my_list))
    new_list.append(my_list)
    return new_list
