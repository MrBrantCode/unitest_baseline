"""
QUESTION:
Write a function `sum_even_recursive` that calculates the sum of all even numbers in a given array using a recursive approach. The function should take two parameters: an array of integers and its length, and return the sum of all even numbers in the array.
"""

def sum_even_recursive(arr, n):
    if n == 0:  
        return 0
    else:
        if arr[n-1] % 2 == 0:  
            return arr[n-1] + sum_even_recursive(arr, n-1)  
        else:
            return sum_even_recursive(arr, n-1)  