"""
QUESTION:
Create a function my_func that accepts a list of integers and returns the maximum value using recursion. The list can contain between 1 and 10^6 integers ranging from -10^9 to 10^9. The function must not use any built-in functions or libraries to find the maximum value and have a time complexity of O(n), where n is the length of the list.
"""

def my_func(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_value = my_func(lst[1:])
        if lst[0] > max_value:
            return lst[0]
        else:
            return max_value