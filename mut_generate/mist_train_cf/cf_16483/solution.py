"""
QUESTION:
Write a function `calculate_area` that calculates the area of a triangle given its base and height. The function should take two integers `base` and `height` as input and return the calculated area using only bitwise operations. The function should have a time complexity of O(1) and a space complexity of O(1).
"""

def calculate_area(base, height):
    # Bitwise multiplication of base and height
    product = base * height
    
    # Divide the product by 2 using right shift
    area = product >> 1
    
    return area