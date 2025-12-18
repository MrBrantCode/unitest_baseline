"""
QUESTION:
Implement a function that takes five dynamic integer inputs from the user, representing the variables a, b, c, d, and e. The function should check two conditions: 

1. If a is greater than b or b is less than c, it should print the product of a, b, and c.
2. If b multiplied by c is greater than a raised to the power of d, it should print the product of a, b, c, and d; otherwise, it should print the sum of a, b, c, d, and e.
"""

def entrance(a, b, c, d, e):
    """
    This function checks two conditions based on the input parameters a, b, c, d, and e.
    
    If a is greater than b or b is less than c, it returns the product of a, b, and c.
    If b multiplied by c is greater than a raised to the power of d, it returns the product of a, b, c, and d; 
    otherwise, it returns the sum of a, b, c, d, and e.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    c (int): The third integer.
    d (int): The fourth integer.
    e (int): The fifth integer.
    
    Returns:
    int: The result based on the conditions.
    """
    
    if a > b or b < c:
        print(a * b * c)
    
    if b * c > a ** d:
        return a * b * c * d
    else:
        return a + b + c + d + e