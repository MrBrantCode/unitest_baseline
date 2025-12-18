"""
QUESTION:
Write a function `simplify_boolean_expression` that simplifies the Boolean expression `a[i] == max || !(max != a[i])`. The function should return the simplified expression as a string.
"""

def simplify_boolean_expression(a, i, max):
    return f"a[{i}] == {max}"