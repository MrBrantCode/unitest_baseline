"""
QUESTION:
Create a program that contains two functions: `factorial_while` and `factorial_tail_recursion`. 

The `factorial_while` function should calculate the factorial of a given non-negative integer `n` using a while loop. 

The `factorial_tail_recursion` function should calculate the factorial of a given non-negative integer `n` using tail recursion. This function should have an optional parameter `acc` with a default value of 1.

Both functions should return an error message if `n` is negative or not an integer.

The program should also include a main function to test these functions with a user-provided number.
"""

def factorial_while(n):
    if not isinstance(n, int) or n < 0:
        return "Error: Factorial is undefined for negative numbers and non-integer values."
    elif n == 0:
        return 1
    else:
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1
        return factorial

def factorial_tail_recursion(n, acc=1):
    if not isinstance(n, int) or n < 0:
        return "Error: Factorial is undefined for negative numbers and non-integer values."
    elif n == 0:
        return acc
    else:
        return factorial_tail_recursion(n - 1, n * acc)