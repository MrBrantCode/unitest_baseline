"""
QUESTION:
Implement the function `try_if(lst)` that takes a list of integers as input and returns a new list where each element is transformed according to the following rules: if the element is even, add 10 to it, and if the element is odd, subtract 5 from it.
"""

def try_if(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            result.append(num + 10)
        else:
            result.append(num - 5)
    return result