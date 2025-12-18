"""
QUESTION:
Write a function named `print_reverse_array` that takes an array of integers as input and prints each element in reverse order without using built-in reverse functions. The function should return an error message if the array contains any negative numbers.
"""

def print_reverse_array(arr):
    for num in arr:
        if num < 0:
            print("Error: Array contains negative numbers")
            return
    for i in range(len(arr) - 1, -1, -1):  
        print(arr[i])