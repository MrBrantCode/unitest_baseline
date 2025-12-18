"""
QUESTION:
Write a function named `second_smallest_and_sum_of_evens` that takes a list of integers as input and returns a tuple. The function should find the second smallest even number in the list and the sum of all even numbers in the list. If there is no second smallest even number, it should return `None` for that value. The function should not use any built-in sorting or statistics functions and should handle negative numbers correctly.
"""

def second_smallest_and_sum_of_evens(lst: list):
    if not lst:
        return None, 0

    min1 = min2 = float('inf')  
    even_sum = 0

    for x in lst:
        if x % 2 == 0:  
            even_sum += x  
            if x < min1:  
                min2 = min1  
                min1 = x  
            elif x < min2 and x != min1:  
                min2 = x  

    return min2 if min2 != float('inf') else None, even_sum