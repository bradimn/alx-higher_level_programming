#!/usr/bin/python3
# 4-new_in_list.py


def new_in_list(my_list, idx, element):
    """Replacing the element in a copied list at a specific position."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    cop = [x for x in my_list]
    cop[idx] = element
    return (cop)