"""
QUESTION:
Create a function `sum_of_squares` that takes two integer parameters `start` and `end` and returns the sum of the squares of all numbers between them, inclusive. The function should satisfy the following conditions: 
- `start` should be less than or equal to `end`. If not, return an error message.
- Both `start` and `end` should be integers. If not, return an error message.
- Both `start` and `end` should be within the range -1000 to 1000 (inclusive). If not, return an error message.
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