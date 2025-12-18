"""
QUESTION:
Create a function named `modify_and_reverse(arr)` that takes an array of integers as input, replaces every even-indexed integer with its factorial (without using the built-in factorial function), and reverses the order of the elements in the array. The function should return the modified array.
"""

def calculate_factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

def modify_and_reverse(arr):
    for i in range(len(arr)):
        if i % 2 == 0:
            arr[i] = calculate_factorial(arr[i])
    arr.reverse()
    return arr