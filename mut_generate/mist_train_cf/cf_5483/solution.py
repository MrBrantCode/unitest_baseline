"""
QUESTION:
Implement a function `sum_of_odds(arr, index, sum)` that recursively calculates the sum of all odd numbers in a given array. The function should have a time complexity of O(n), where n is the length of the array, and should not use any built-in functions or libraries for summation or checking odd numbers. The array can contain both positive and negative integers, duplicates, and be empty, and the sum can be zero if there are no odd numbers in the array.
"""

def sum_of_odds(arr, index=0, sum=0):
    # Base case: if index is equal to the length of the array, return the sum
    if index == len(arr):
        return sum

    # Recursive case: check if the current element is odd
    if arr[index] % 2 != 0:
        sum += arr[index]

    # Call the function recursively for the next index
    return sum_of_odds(arr, index + 1, sum)