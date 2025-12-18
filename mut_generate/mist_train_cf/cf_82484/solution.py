"""
QUESTION:
Design a function called `find_average` that finds all the numbers between 0 and a given number `n` (inclusive) that are divisible by both 3 and 5, and then calculates and returns their average. The function should be efficient and should not store all the numbers in memory.
"""

def find_average(n):
    """
    Finds the average of numbers between 0 and n (inclusive) that are divisible by both 3 and 5.
    
    Args:
    n (int): The upper limit of the range (inclusive).
    
    Returns:
    float: The average of the numbers divisible by both 3 and 5.
    """
    total, count = 0, 0
    for i in range(0, n + 1, 15):
        if i % 3 == 0 and i % 5 == 0:
            total += i
            count += 1
    return total / count if count != 0 else 0