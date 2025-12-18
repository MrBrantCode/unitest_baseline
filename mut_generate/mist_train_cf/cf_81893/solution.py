"""
QUESTION:
Create a function `median_of_five` that takes five numbers as input and returns the median of those numbers. The numbers are not guaranteed to be in any particular order, and the function should be able to handle this. The median is the middle value in the ordered list of numbers, which in this case is the third value since there are five numbers.
"""

def median_of_five(a, b, c, d, e):
    numbers = [a, b, c, d, e]
    numbers.sort()
    
    return numbers[2]