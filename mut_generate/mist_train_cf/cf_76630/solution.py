"""
QUESTION:
Given an array of numbers and an integer k, implement the function `smallest_k_odd_numbers(arr, k)` that removes all the even numbers from the array and returns k smallest odd numbers from the remaining odd numbers in the array. If there are fewer than k odd numbers in the array, return all the odd numbers.
"""

def smallest_k_odd_numbers(arr, k):
    # Use list comprehension to filter out the even numbers
    odd_numbers = [num for num in arr if num % 2 != 0]
    
    # Sort the odd numbers in ascending order and return the first k numbers
    return sorted(odd_numbers)[:k]