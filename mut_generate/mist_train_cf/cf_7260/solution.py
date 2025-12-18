"""
QUESTION:
Create a function called `shuffle_list` that takes a list of integers as input, returns a new list with all even numbers before odd numbers (preserving their original order), and does not use any built-in shuffling functions. The length of the input list should not exceed 100 elements, and the function should have a time complexity of O(n). The function should also ensure the output list does not contain any duplicates.
"""

def shuffle_list(lst):
    even_nums = []
    odd_nums = set()

    for num in lst:
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.add(num)

    return even_nums + list(odd_nums)