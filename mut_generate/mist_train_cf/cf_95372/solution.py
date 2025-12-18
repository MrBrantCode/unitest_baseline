"""
QUESTION:
Write a function `recursive_product` that takes a list of integers as input and returns their product. Implement the multiplication using a recursive approach, without using the `*` operator or built-in multiplication functions. The function should handle lists of any size, including empty lists, and lists containing negative numbers. The time complexity should be O(n), where n is the length of the input list.
"""

def recursive_product(lst):
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
            return 0 - multiply(x, -y)

    if len(lst) == 0:
        return 1
    elif len(lst) == 1:
        return lst[0]
    else:
        return multiply(lst[0], recursive_product(lst[1:]))