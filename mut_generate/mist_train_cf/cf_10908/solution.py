"""
QUESTION:
Write a function called `find_maximum` that calculates the maximum value of an input array under the following conditions: 
- If the array is empty, return None.
- If the array contains duplicate maximum values, return the first occurrence of the maximum value.
- If the array contains only negative values, return the maximum negative value.
- If the array contains both positive and negative values, return the maximum positive value.
- If the array contains only zero values, return zero.
The function should take an array as input and return the maximum value according to the conditions above.
"""

def find_maximum(array):
    if len(array) == 0:
        return None

    max_value = float('-inf')  # initialize max_value as negative infinity
    max_negative = float('-inf')  # initialize max_negative as negative infinity
    has_positive = False
    has_zero = False

    for num in array:
        if num == 0:
            has_zero = True
        elif num > 0:
            has_positive = True
            max_value = max(max_value, num)
        else:
            max_negative = max(max_negative, num)

    if has_zero:
        return 0
    elif has_positive:
        return max_value
    else:
        return max_negative