"""
QUESTION:
Write a function named `get_unique_odd_numbers` that takes a list of integers as input, removes duplicates, and returns only the odd numbers in descending order. Do not use any built-in functions or libraries, and ensure the time complexity is O(n^2) or less.
"""

def get_unique_odd_numbers(nums):
    unique_odds = []
    for num in nums:
        if num % 2 != 0 and num not in unique_odds:
            unique_odds.append(num)
    
    unique_odds.sort(reverse=True)
    return unique_odds