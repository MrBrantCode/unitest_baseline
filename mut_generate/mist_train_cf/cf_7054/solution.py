"""
QUESTION:
Create a function `sum_of_squares` that takes two parameters `start` and `end`, both of which should be integers between -1000 and 1000 (inclusive), where `start` is less than or equal to `end`. The function should return the sum of the squares of all numbers between `start` and `end`, inclusive. If any of these conditions are not met, the function should return an error message.
"""

def sum_of_squares(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        return "Error: Parameters should be integers."
    
    if start > end:
        return "Error: Start parameter should be less than the end parameter."
    
    if start < -1000 or end > 1000:
        return "Error: Parameters should be within the range -1000 to 1000 (inclusive)."
    
    result = 0
    for num in range(start, end + 1):
        result += num**2
    
    return result