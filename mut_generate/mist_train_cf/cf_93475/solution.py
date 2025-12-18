"""
QUESTION:
Write a recursive function `find_max` that takes a list of numbers and returns a tuple containing the maximum number in the list and its index. The function should not use any built-in functions like max() or index().
"""

def find_max(numbers, index=0, max_num=None, max_index=None):
    if index == len(numbers):
        return max_num, max_index
    else:
        if max_num is None or numbers[index] > max_num:
            max_num = numbers[index]
            max_index = index
        return find_max(numbers, index+1, max_num, max_index)