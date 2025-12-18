"""
QUESTION:
Write a function named `get_even_numbers` that takes an array of integers as input, where the length of the array is between 1 and 10^5 (inclusive), and the integers range from -10^9 to 10^9. The function should return a new array containing only the even numbers from the input array, sorted in ascending order.
"""

def get_even_numbers(arr):
    return sorted([num for num in arr if num % 2 == 0])