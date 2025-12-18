"""
QUESTION:
Create a function `remove_duplicates` that takes a list of numbers and returns a new list with all elements that occur more than twice removed, sorted in descending order. The input list will contain at most 10^5 elements and at least one element.
"""

def remove_duplicates(numbers):
    count = {}
    for num in numbers:
        count[num] = count.get(num, 0) + 1

    return sorted([num for num in set(numbers) if count[num] <= 2], reverse=True)