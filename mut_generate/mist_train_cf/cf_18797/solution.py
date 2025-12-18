"""
QUESTION:
Generate a function `recursive_product` that takes a list of integers as input and returns the product of all the integers in the list. The function should use a recursive approach, without using any built-in multiplication functions or operators, and should handle edge cases such as empty lists, lists with a single element, and lists with negative numbers. The function should also be efficient for large lists, with a time complexity of O(n), where n is the length of the input list, and should only use the function call stack to store necessary information.
"""

def recursive_product(lst):
    if len(lst) == 0:  
        return 1
    elif len(lst) == 1:  
        return lst[0]
    elif len(lst) == 2:  
        def add(x, y):
            if y == 0:
                return x
            elif y > 0:
                return add(x + 1, y - 1)
            else:
                return add(x - 1, y + 1)
        def multiply(x, y):
            if y == 0:
                return 0
            elif y > 0:
                return add(x, multiply(x, y - 1))
            else:
                return -multiply(x, -y)
        return multiply(lst[0], lst[1])
    elif lst[0] < 0 and lst[1] < 0:  
        return recursive_product([-1 * lst[0]] + lst[1:])
    else:
        def add(x, y):
            if y == 0:
                return x
            elif y > 0:
                return add(x + 1, y - 1)
            else:
                return add(x - 1, y + 1)
        def multiply(x, y):
            if y == 0:
                return 0
            elif y > 0:
                return add(x, multiply(x, y - 1))
            else:
                return -multiply(x, -y)
        return multiply(lst[0], recursive_product(lst[1:]))