"""
QUESTION:
Create a function called `calculate_average` that takes a 2D array of numbers as input, calculates the sum of the numbers across all the sub-arrays, and returns the average of those sums. The function should ignore empty sub-arrays and non-numeric values within the sub-arrays, handle large arrays efficiently without causing memory or performance issues, and have a time complexity of O(n), where n is the total number of elements in all the sub-arrays.
"""

def calculate_average(arr):
    total_sum = 0
    total_elements = 0

    for sub_arr in arr:
        if not sub_arr:
            continue

        for num in sub_arr:
            if isinstance(num, (int, float)):
                total_sum += num
                total_elements += 1

    if total_elements == 0:
        return 0  

    average = total_sum / total_elements
    return average