"""
QUESTION:
Write a function `count_odd_numbers` that takes an array of integers as input and returns the count of unique odd numbers in the array that are greater than 10 and less than 100, excluding negative numbers and duplicates. The solution should have a time complexity of O(n), where n is the size of the input array, and should not use any built-in functions or methods for finding odd numbers or counting elements.
"""

def count_odd_numbers(arr):
    odd_numbers = set()
    for num in arr:
        if num > 0 and num % 2 != 0 and num > 10 and num < 100:
            odd_numbers.add(num)
    
    return len(odd_numbers)