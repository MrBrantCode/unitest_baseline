"""
QUESTION:
Design a function `count_occurrences` that counts the number of occurrences of each element in a given list of integers. The function should have a time complexity of O(n) and a space complexity of O(k), where n is the number of elements in the list and k is the number of unique elements. The function should use only a single loop to iterate through the list and not use any built-in functions or data structures that directly solve the problem.
"""

def count_occurrences(numbers):
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts