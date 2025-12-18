"""
QUESTION:
Implement a function named `cube_and_sum` that takes an array of integers as input. The function should cube each odd integer and square each even integer in the array, sort the resulting array in ascending order, and then calculate the running sum of the sorted array. Return the array of running sums as the result. The function should handle arrays of any length and should not include any input validation.
"""

def cube_and_sum(array):
    # cube if odd, square if even and sort
    array = sorted([x**3 if x % 2 != 0 else x**2 for x in array])
    # calculate the running sum
    for i in range(1, len(array)):
        array[i] += array[i - 1]
    return array