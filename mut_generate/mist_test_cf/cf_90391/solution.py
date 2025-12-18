"""
QUESTION:
Write a function named `get_unique_odd_numbers` that takes a list of integers as input and returns a list of unique odd numbers from the input list in descending order. The function must not use any built-in functions or libraries and must have a time complexity of O(n^2) or less.
"""

def get_unique_odd_numbers(nums):
    unique_odds = []
    for num in nums:
        if num % 2 != 0 and num not in unique_odds:
            unique_odds.append(num)
    
    unique_odds.sort(reverse=True)
    return unique_odds