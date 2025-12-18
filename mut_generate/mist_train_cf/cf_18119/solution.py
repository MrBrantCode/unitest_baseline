"""
QUESTION:
Write a function `highest_lowest_prime(numbers)` that takes a list of positive integers as input. The function should return a tuple containing the highest and lowest numbers in the list. If the list has less than two elements, return `None`. The order of the numbers in the tuple depends on two conditions: (1) if the highest number is divisible by the lowest number, return `(highest, lowest)`, otherwise check (2) if the lowest number is prime, return `(lowest, highest)` if prime, otherwise return `(highest, lowest)`.
"""

def highest_lowest_prime(numbers):
    if len(numbers) < 2:
        return None
    
    highest = max(numbers)
    lowest = min(numbers)
    
    if highest % lowest == 0:
        return (highest, lowest)
    
    for i in range(2, int(lowest ** 0.5) + 1):
        if lowest % i == 0:
            return (highest, lowest)
    
    return (lowest, highest)