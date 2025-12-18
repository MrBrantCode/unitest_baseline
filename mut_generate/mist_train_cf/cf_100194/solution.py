"""
QUESTION:
Create a function `list_comprehension` that takes a list of integers as input and returns a list of integers. The function should use a lambda function and a list comprehension with a conditional and ternary expression to process the input list. The list comprehension should include elements from the input list that satisfy the condition `i % 2 == 0`, and apply the ternary expression `i if i > 10 else i**2` to each included element.
"""

def list_comprehension(x):
    return [i if i > 10 else i**2 for i in x if i % 2 == 0]