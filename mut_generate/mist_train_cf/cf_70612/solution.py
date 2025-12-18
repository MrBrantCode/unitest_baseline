"""
QUESTION:
Given a list of rectangle breadths, write a function `rectangle_lengths` that returns a list of rectangle lengths where the area of each rectangle is a perfect square and the breadth is half of the length.
"""

def rectangle_lengths(breadths):
    lengths = []
    for breadth in breadths:
        length = breadth * 2  
        area = length * breadth 
        if (area ** 0.5).is_integer():
            lengths.append(length)
    return lengths