"""
QUESTION:
Write a function named `count_odd_numbers` that takes an array of integers as input and returns the number of unique odd integers greater than 10 and less than 100, excluding negative numbers and duplicates. The function should have a time complexity of O(n) and should not use any built-in functions or methods for finding odd numbers or counting elements. The input array can contain up to 1 million elements and may include duplicate numbers.
"""

def count_odd_numbers(arr):
    unique_odd_numbers = set()
    for num in arr:
        if num > 0 and num % 2 != 0 and num > 10 and num < 100:
            unique_odd_numbers.add(num)
    return len(unique_odd_numbers)