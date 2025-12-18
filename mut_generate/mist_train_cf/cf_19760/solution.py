"""
QUESTION:
Write a function called `calculate_average` that takes a 2D array of numbers as input and returns the average of the sums of the numbers across all the arrays. The function should ignore empty sub-arrays and non-numeric values within the sub-arrays. It should also be able to handle large arrays with millions of elements efficiently, with a time complexity of O(n), where n is the total number of elements in all the arrays.
"""

def entrance(arr):
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