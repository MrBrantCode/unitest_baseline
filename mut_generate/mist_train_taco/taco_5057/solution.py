"""
QUESTION:
Write a function that solves an algebraic expression given as a string. 

* The expression can include only sums and products. 

* The numbers in the expression are in standard notation (NOT scientific).

* In contrast, the function should return a string with the calculated value given in scientific notation with 5 decimal digits. 

# Example:
```python
strexpression = "5 * 4 + 6"
sum_prod(strexpression) = "2.60000e+01"
```
"""

def evaluate_expression(expression: str) -> str:
    """
    Evaluates an algebraic expression given as a string and returns the result in scientific notation with 5 decimal digits.

    Parameters:
    expression (str): The algebraic expression to be evaluated, which can include sums and products of numbers in standard notation.

    Returns:
    str: The evaluated value in scientific notation with 5 decimal digits.
    """
    return '%.5e' % eval(expression)