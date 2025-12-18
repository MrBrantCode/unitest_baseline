"""
QUESTION:
Implement a function named `sum_of_elements` that calculates the sum of all unique elements in a given array. The function should not use any built-in functions or libraries to calculate the sum, should not modify the original array, and should have a time complexity of O(n), where n is the number of elements in the array.
"""

def sum_of_elements(array):
    sum = 0
    seen = set()
    for num in array:
        if num not in seen:
            sum += num
            seen.add(num)
    return sum