"""
QUESTION:
Implement a function `mean(arr)` that calculates the mean of a given array 'arr' from scratch without using any built-in functions or methods. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array. The array can be empty.
"""

def calculate_mean(arr):
    n = len(arr)
    if n == 0:
        return None
    sum = 0
    for num in arr:
        sum += num
    return sum / n