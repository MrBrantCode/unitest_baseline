"""
QUESTION:
Implement a function `bubble_sort_descending_odd` that sorts the odd numbers in a list of integers in descending order, while keeping the even numbers in their original positions. The function should take a list of integers as input and return the modified list.
"""

def bubble_sort_descending_odd(lst):
    n = len(lst)
    odd_nums = sorted([num for num in lst if num % 2 != 0], reverse=True)
    odd_nums_idx = 0
    for i in range(n):
        if lst[i] % 2 != 0:
            lst[i] = odd_nums[odd_nums_idx]
            odd_nums_idx += 1
    return lst