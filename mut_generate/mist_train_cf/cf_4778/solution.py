"""
QUESTION:
Implement a function `sum_of_cubes(arr)` that calculates the sum of the cubes of the integers in a given list `arr` and returns the result rounded to the nearest integer. The function should handle exceptions that may occur during calculation and have a time complexity of O(n) and space complexity of O(1).
"""

def sum_of_cubes(arr):
    sum_cubes = 0
    for num in arr:
        try:
            sum_cubes += num ** 3
        except Exception:
            return None
    
    return round(sum_cubes)