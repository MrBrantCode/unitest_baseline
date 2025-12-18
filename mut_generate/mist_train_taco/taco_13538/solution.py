"""
QUESTION:
I need some help with my math homework. I have a number of problems I need to return the derivative for.

They will all be of the form:  
ax^b,  
A and B are both integers, but can be positive or negative.
Note: 
  - if b is 1, then the equation will be ax.  
  - if b is 0, then the equation will be 0.  
  
Examples:
  3x^3   -> 9x^2  
  3x^2   -> 6x  
  3x     -> 3  
  3      -> 0  
  3x^-1  -> -3x^-2  
  -3x^-2 -> 6x^-3  

If you don't remember how derivatives work, here's a link with some basic rules: https://www.mathsisfun.com/calculus/derivatives-rules.html
"""

def calculate_derivative(a: int, b: int) -> str:
    if b == 0:
        return '0'
    elif b == 1:
        return str(a)
    else:
        new_coefficient = a * b
        new_exponent = b - 1
        if new_exponent == 1:
            return f'{new_coefficient}x'
        else:
            return f'{new_coefficient}x^{new_exponent}'