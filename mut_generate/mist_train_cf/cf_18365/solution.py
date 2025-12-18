"""
QUESTION:
Write a function `generate_integer_list(start, end)` that generates a list of integers between `start` and `end` (inclusive) in descending order, with no duplicates. The function should be able to handle a range of up to 10^9 and have a time complexity of O(n log n).
"""

def generate_integer_list(start, end):
    unique_values = set()
    integers = []

    for i in range(start, end + 1):
        if i not in unique_values:
            unique_values.add(i)
            integers.append(i)

    integers.sort(reverse=True)
    return integers