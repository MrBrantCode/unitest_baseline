"""
QUESTION:
Write a function `swap_even_and_odd(my_list)` that takes a list of integers as input and returns a new list where the positions of even and odd elements are swapped. The function should swap the elements at even indices with the elements at odd indices. The input list is 1-indexed for the purpose of determining even and odd indices.
"""

def swap_even_and_odd(my_list):
    for i in range(len(my_list)-1):
        if i % 2 == 0 and my_list[i] % 2 != 0 and my_list[i+1] % 2 == 0:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    return my_list