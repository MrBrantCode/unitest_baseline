"""
QUESTION:
Write a function called `shuffle_list` that takes a list of integers as input. The function should return a new list with all even numbers before odd numbers, preserving their original order within their respective groups, without using any built-in shuffling functions or libraries. The original list should remain unchanged. The function should have a time complexity of O(n), where n is the length of the input list, and the output list should not contain any duplicates.
"""

def shuffle_list(lst):
    even_nums = []
    odd_nums = []

    # Split the list into even and odd numbers
    for num in lst:
        if num % 2 == 0 and num not in even_nums:
            even_nums.append(num)
        elif num % 2 != 0 and num not in odd_nums:
            odd_nums.append(num)

    # Concatenate the even and odd numbers
    shuffled_list = even_nums + odd_nums

    return shuffled_list