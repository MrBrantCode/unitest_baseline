"""
QUESTION:
Write a function `fourth_highest_even_element` that takes a list of integers as input and returns the fourth highest even number in the list. If there are less than four even numbers in the list, return "Not enough even numbers". The function should be able to handle both positive and negative integers, and should not use built-in functions like max() or sort().
"""

def fourth_highest_even_element(l: list):
    max1, max2, max3, max4 = float('-inf'), float('-inf'), float('-inf'), float('-inf')
    for x in l:
        if x % 2 == 0:
            if x > max1:
                max4 = max3
                max3 = max2
                max2 = max1
                max1 = x
            elif x != max1 and x > max2:
                max4 = max3
                max3 = max2
                max2 = x
            elif x != max1 and x != max2 and x > max3:
                max4 = max3
                max3 = x
            elif x != max1 and x != max2 and x != max3 and x > max4:
                max4 = x
    if max4 == float("-inf"): 
        return "Not enough even numbers"
    else:
        return max4