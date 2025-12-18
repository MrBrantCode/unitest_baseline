"""
QUESTION:
Write a function named shuffle_list that takes a list of integers as input, shuffles it such that all even numbers come before odd numbers while preserving their original order, and returns the shuffled list without modifying the original list. The function should not use any built-in shuffling functions or libraries, have a time complexity of O(n) or better, and support lists with a maximum length of 100 elements.
"""

def shuffle_list(lst):
    even_lst = []
    odd_lst = []

    for num in lst:
        if num % 2 == 0:
            even_lst.append(num)
        else:
            odd_lst.append(num)

    return even_lst + odd_lst