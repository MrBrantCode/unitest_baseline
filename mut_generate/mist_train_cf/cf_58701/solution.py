"""
QUESTION:
Implement a recursive function `change(test, n)` that takes two parameters, `test` and `n`, both of which can be integer or floating point numbers. 

The function should output a string message and return a result based on the value of `test`:
- If `test` is greater than 10, output 'Your input is greater than 10' and return `test * n`.
- If `test` is less than 10, output 'Your input is less than 10' and return `test / n`. The function must handle division by zero errors.
- If `test` is equal to 10, output 'Your input is 10' and return the remainder of `test` divided by `n`. The function must also handle the case where `n` is zero.

The function should use recursion to avoid infinite loops and handle all possible input scenarios.
"""

def change(test, n):
  if n == 0:
    print("n can't be 0!")
    return None

  if test > 10:
    print('Your input is greater than 10')
    return test * n if n > 1 else change(test-1, n)
  elif test < 10:
    print('Your input is less than 10')
    return test / n if n > 1 else change(test, n-1)
  elif test == 10:
    print('Your input is 10')
    return test % n if n > 1 else change(test-1, n)