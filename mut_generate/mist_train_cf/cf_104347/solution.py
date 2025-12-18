"""
QUESTION:
Write a function named `remove_duplicates` that takes a list of numbers as input and returns a new list containing the numbers that occur not more than twice, sorted in descending order. The input list contains at most 10^5 elements and at least one element.
"""

def remove_duplicates(numbers):
    count = {}
    for num in numbers:
        count[num] = count.get(num, 0) + 1

    result = [num for num in numbers if count[num] <= 2]
    return sorted(result, reverse=True)