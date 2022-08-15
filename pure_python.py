from tkinter import LAST


my_list = [1, 2, 3]


def add_to_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl


nl = add_to_list(my_list, 4)
print(my_list)
print(nl)
