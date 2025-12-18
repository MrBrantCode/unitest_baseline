"""
QUESTION:
Create a function `my_func` that accepts a list of integers and returns the maximum value. The function must use recursion to find the maximum value. The list length will be between 1 and 10^6, and the integers in the list can range from -10^9 to 10^9. Do not use any built-in functions or libraries to find the maximum value, and ensure the time complexity of your solution is O(n), where n is the length of the list.
"""

def entance(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_value = entance(lst[1:])
        if lst[0] > max_value:
            return lst[0]
        else:
            return max_value