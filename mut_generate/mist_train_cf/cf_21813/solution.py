"""
QUESTION:
Create a function named `shuffle_list` that takes a list of integers as an argument, shuffles it, and returns the shuffled list without modifying the original list. The shuffled list should have all even numbers before odd numbers, with the order of the even numbers and odd numbers preserved. The function should not use any built-in functions or libraries for shuffling, and its time complexity should be O(n) or better. The input list should not exceed 100 elements.
"""

def shuffle_list(lst):
    even_lst = []
    odd_lst = []

    for num in lst:
        if num % 2 == 0:
            even_lst.append(num)
        else:
            odd_lst.append(num)

    shuffled_lst = even_lst + odd_lst

    return shuffled_lst