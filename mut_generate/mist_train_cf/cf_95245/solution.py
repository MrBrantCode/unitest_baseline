"""
QUESTION:
Implement the function `count_occurrences(numbers)` that takes a list of integers as input and returns a dictionary where the keys are the unique elements in the list and the values are their respective counts. The solution should have a time complexity of O(n) and a space complexity of O(k), where n is the number of elements in the list and k is the number of unique elements. Use only a single loop to iterate through the list and do not use any built-in functions or data structures that directly solve the problem.
"""

def count_occurrences(numbers):
    counts = {}  # Empty dictionary to store count of each element
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts