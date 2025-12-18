"""
QUESTION:
Write a function named `sort_tuples` that takes a list of tuples, where each tuple contains a string and an integer, and returns the sorted list in descending order of integers. If multiple tuples have the same integer, they should be sorted in descending order of strings.
"""

def sort_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: (-x[1], x[0]), reverse=False)