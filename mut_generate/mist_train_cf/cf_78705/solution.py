"""
QUESTION:
Create a function `solve_problem` that takes a list of numbers as input, sorts the list in ascending order, calculates the average, and returns a dictionary containing the average and a sorted list of numbers that are less than or equal to the average. The function should handle lists with at least one element.
"""

def solve_problem(arr):
    arr.sort()
    avg = sum(arr) / len(arr)
    result_array = [n for n in arr if n <= avg]
    result = {
        "Average": avg,
        "Sorted_Array": result_array
    }
    return result