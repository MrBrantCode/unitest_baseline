"""
QUESTION:
Implement a function `sum(numbers)` that calculates the sum of a list of numbers with the following restrictions:

- The function should return -1 if the input list is empty.
- The function should return -1 if any number in the list is negative.
- The function should return -1 if the sum of the numbers exceeds 100.
- The time complexity should be O(n), where n is the length of the input list.
- The space complexity should be O(1).
"""

def sum_of_numbers(numbers):
    if len(numbers) == 0:
        return -1
        
    total_sum = 0
    for n in numbers:
        if n < 0 or total_sum + n > 100:
            return -1
        total_sum += n
        
    return total_sum