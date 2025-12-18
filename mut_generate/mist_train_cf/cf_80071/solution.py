"""
QUESTION:
Create a function called `second_smallest_odd_and_second_largest_even` that takes a list of integers as input and returns a tuple containing the second smallest odd number and the second largest even number. The function should handle cases where there is no second smallest odd number or second largest even number by returning "No Second Smallest Odd Number" or "No Second Largest Even Number" respectively.
"""

def second_smallest_odd_and_second_largest_even(l):
    min1, min2, max1, max2 = float('inf'), float('inf'), float('-inf'), float('-inf')
    for x in l:
        if x % 2 != 0: 
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2 and x != min1:
                min2 = x
        else: 
            if x > max1:
                max2 = max1
                max1 = x
            elif x > max2 and x != max1:
                max2 = x
    return (min2 if min2 != float('inf') else "No Second Smallest Odd Number", 
            max2 if max2 != float('-inf') else "No Second Largest Even Number")