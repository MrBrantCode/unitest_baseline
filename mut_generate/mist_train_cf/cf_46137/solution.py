"""
QUESTION:
Write a function named `multiply` that takes two parameters, x and y. The function should multiply x and y and return the result. It should handle non-numeric inputs by returning the message 'Please provide numeric inputs only.' The function should be able to handle arbitrarily large integers.
"""

def multiply(x, y):
    try:
        x = int(x)
        y = int(y)
        return x * y 
    except ValueError as ve:
        return 'Please provide numeric inputs only.'