"""
QUESTION:
The factorial of a number, `n!`, is defined for whole numbers as the product of all integers from `1` to `n`. 

For example, `5!` is `5 * 4 * 3 * 2 * 1 = 120`

Most factorial implementations use a recursive function to determine the value of `factorial(n)`. However, this blows up the stack for large values of `n` - most systems cannot handle stack depths much greater than 2000 levels.

Write an implementation to calculate the factorial of arbitrarily large numbers, *without recursion.*

# Rules

* `n < 0` should return `nil`/  `None`
* `n = 0` should return `1`
* `n > 0` should return `n!`

# Note

Codewars limits the amount of data it will send back and forth, which may introduce a false ceiling for how high of a value of `n` it will accept. All tests use values less than this limit.
"""

def calculate_factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result