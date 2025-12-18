"""
QUESTION:
Write a function `get_mean(numbers)` that calculates the mean of a list of numbers. The input list may contain up to 1 million numbers. The function should return the mean rounded to 2 decimal places. The function must handle the following edge cases: return `None` if the input list is empty, contains non-numeric elements, or contains negative numbers. The function should also handle large input lists efficiently without exceeding memory limits.
"""

def entrance(numbers):
    if len(numbers) == 0:
        return None
    
    sum = 0
    count = 0
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            return None
        if num < 0:
            return None
        
        sum += num
        count += 1
    
    if count == 0:
        return None
    
    return round(sum/count, 2)