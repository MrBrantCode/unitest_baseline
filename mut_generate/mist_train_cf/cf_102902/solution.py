"""
QUESTION:
Design a function called `separate_even_odd` that takes a list of integers as input and returns two separate lists: one containing all the even numbers and the other containing all the odd numbers. The input list can contain any number of integers, and the order of numbers in the output lists should be the same as their order in the input list.
"""

def separate_even_odd(lst):
    even_nums = []
    odd_nums = []
    for num in lst:
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)
    return (even_nums, odd_nums)