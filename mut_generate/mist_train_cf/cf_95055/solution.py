"""
QUESTION:
Construct a function `highest_lowest_prime(numbers)` that takes a list of positive integers as input and returns a tuple of the highest and lowest numbers. If the highest number is divisible by the lowest number, the function should return the tuple in the order (highest, lowest). If the highest number is not divisible by the lowest number, the function should return the tuple in the order (highest, lowest) if the lowest number is not prime, and (lowest, highest) if the lowest number is prime. If the list is empty or contains only one element, the function should return None.
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