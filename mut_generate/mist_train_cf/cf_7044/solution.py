"""
QUESTION:
Create a function `sort_positive_descending(arr)` that takes an array of integers as input, sorts the positive elements in descending order, and removes duplicates. The function should have a time complexity of O(n log n) or better. The array can contain at most 10^6 elements, and the elements will be positive integers between 1 and 10^9 (inclusive).
"""

def sort_positive_descending(arr):
    count_dict = {}
    for num in arr:
        if num > 0:
            count_dict[num] = count_dict.get(num, 0) + 1

    unique_list = []
    for key, value in count_dict.items():
        unique_list.extend([key] * value)

    unique_list.sort(reverse=True)
    return unique_list