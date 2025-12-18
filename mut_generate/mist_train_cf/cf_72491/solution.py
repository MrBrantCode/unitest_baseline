"""
QUESTION:
Write a function named `calculate_even_average` that takes a list of numbers as input and returns the average of the even numbers in the list. The function should handle the case when there are no even numbers in the list and avoid division by zero error. The function should have a time complexity of O(n), where n is the number of elements in the list.
"""

def calculate_even_average(nbrs):
    total = 0
    count = 0
    for i in range(len(nbrs)):
        if nbrs[i] % 2 == 0:
            total += nbrs[i]
            count += 1
    return total / count if count != 0 else 0