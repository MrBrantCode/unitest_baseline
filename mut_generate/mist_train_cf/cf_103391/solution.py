"""
QUESTION:
Write a function called `average_of_non_negative_numbers` that calculates the average of a list of integers, excluding any negative numbers. The function should return 0 if all numbers in the list are negative.
"""

def average_of_non_negative_numbers(numbers):
    total = 0
    count = 0
    
    for num in numbers:
        if num < 0:
            continue
        total += num
        count += 1
    
    if count == 0:
        return 0
    
    return total / count