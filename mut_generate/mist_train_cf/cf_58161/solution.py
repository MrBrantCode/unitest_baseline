"""
QUESTION:
Write a function `median(n: list)` that calculates the median of a list of numbers without using any built-in Python functions. The function should handle both cases where the list has an odd number of elements and where it has an even number of elements. If the list is odd, the function should return the middle element. If the list is even, the function should return the average of the two middle elements.
"""

def median(n: list):
    # Sorting the list in Ascending order
    n.sort()

    # Finding the position of the median
    if len(n) % 2 == 0: 
        mid1 = len(n) // 2
        mid2 = (len(n) // 2) - 1
        # If the list is even, the median is the average of the two middle numbers
        median = (n[mid1] + n[mid2]) / 2
    else: 
        mid = len(n) // 2
        # If the list is odd, the median is the middle number
        median = n[mid]
  
    return median