"""
QUESTION:
Implement a function `arithmetic_sum_with_factorials(a, b)` that calculates the sum of factorials for integers in the range from `a` to `b` (inclusive) while handling the following conditions and restrictions:

- Both `a` and `b` must be integers.
- `a` must be greater than or equal to 2.
- `b` must be less than or equal to 6.
- `a` must be less than or equal to `b`.
 
The function should return the sum of factorials for the valid range or an error message if any of the conditions are not met.
"""

def arithmetic_sum_with_factorials(a, b):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
            
    # check if a and b are integers
    if not isinstance(a, int) or not isinstance(b, int):
        return "Error: a and b must be integers."
    # check if a < 2 or b > 6
    elif a < 2 or b > 6:
        return "Error: a must be greater than or equal to 2 and b must be less than or equal to 6."
    # check if a > b
    elif a > b:
        return "Error: a must be less than or equal to b."
    else:
        # calculate arithmetic sum
        total = 0
        for num in range(a, b + 1):
            total += factorial(num)
        return total