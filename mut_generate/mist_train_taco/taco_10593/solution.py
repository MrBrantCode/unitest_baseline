"""
QUESTION:
Just like in the ["father" kata](http://www.codewars.com/kata/find-fibonacci-last-digit/), you will have to return the last digit of the nth element in the Fibonacci sequence (starting with 1,1, to be extra clear, not with 0,1 or other numbers).

You will just get much bigger numbers, so good luck bruteforcing your way through it ;)
```python
last_fib_digit(1) == 1
last_fib_digit(2) == 1
last_fib_digit(3) == 2
last_fib_digit(1000) == 5
last_fib_digit(1000000) == 5
```
``` haskell
lastFibDigit       1 == 1
lastFibDigit       2 == 1
lastFibDigit       3 == 2
lastFibDigit    1000 == 5
lastFibDigit 1000000 == 5
```
"""

def get_last_digit_of_nth_fibonacci(n: int) -> int:
    """
    Returns the last digit of the nth Fibonacci number.

    Parameters:
    n (int): The position in the Fibonacci sequence.

    Returns:
    int: The last digit of the nth Fibonacci number.
    """
    # The last digits of Fibonacci numbers repeat every 60 numbers
    last_digits = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]
    return last_digits[n % 60]