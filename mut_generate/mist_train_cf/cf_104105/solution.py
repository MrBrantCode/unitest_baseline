"""
QUESTION:
Create a function `add_integers` that takes two parameters `a` and `b`, checks if both are integers, and prints their sum. The function should also handle the following conditions: 
- If `a` is a negative number, print an error message.
- If `b` is zero, print an error message.
- If the sum of `a` and `b` is a prime number, print a message indicating that.
The function should not return any values, only print the results or error messages.
"""

def add_integers(a, b):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    if not isinstance(a, int) or not isinstance(b, int):
        print("Both parameters must be integers.")
        return

    if a < 0:
        print("The first parameter cannot be a negative number.")
        return

    if b == 0:
        print("The second parameter cannot be zero.")
        return

    result = a + b
    print("The sum of {} and {} is {}".format(a, b, result))

    if is_prime(result):
        print("The sum is a prime number.")