"""
QUESTION:
Create a function named `sort_even` that takes a list of integers as input and returns a new list. The function should maintain the elements at odd indices in their initial state and sort the elements at even indices. If the even-indexed elements are negative, they should be sorted in descending order; otherwise, they should be sorted in ascending order. The sorted even-indexed elements should retain their original positions in the sequence.
"""

def sort_even(l: list):
    evens = [l[i] for i in range(0, len(l), 2)]
    odds = [l[i] for i in range(1, len(l), 2)]
    evens.sort(key=lambda x: -x if x < 0 else x)
    new_list = [None] * len(l)
    new_list[::2] = evens
    new_list[1::2] = odds
    return new_list