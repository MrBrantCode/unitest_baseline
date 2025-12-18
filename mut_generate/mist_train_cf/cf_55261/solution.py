"""
QUESTION:
Create a function `pendulum_sort` that rearranges a list of strings to create a pendulum-style sequence while preserving the original order of unique elements. The pendulum sequence is achieved by taking the first unique element, then the last unique element, the second unique element, the second to last unique element, and so on. The function should remove duplicates and maintain the relative order of the unique elements based on their first occurrence in the original list.
"""

def pendulum_sort(lst):
    sorted_set = list(sorted(set(lst), key=lst.index))
    left_side = sorted_set[::2]
    right_side = sorted_set[1::2][::-1]
    return left_side + right_side