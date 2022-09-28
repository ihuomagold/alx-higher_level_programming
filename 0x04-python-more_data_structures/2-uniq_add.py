#!/usr/bin/python3
def uniq_add(my_list=[]):
    copy = []
    for x in sorted(set(my_list)):
        copy.append(x)
    return sum(copy)
