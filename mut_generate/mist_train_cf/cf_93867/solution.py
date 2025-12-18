"""
QUESTION:
Create a function `add_integers` that takes two parameters `a` and `b`. This function should first check if both `a` and `b` are integers. If either of them is not an integer, it should print an error message and exit. The function should also check for the following conditions and print the corresponding error messages: 
- `a` is a negative number
- `b` is zero

If all checks pass, the function should print the sum of `a` and `b`. Additionally, if the sum of `a` and `b` is a prime number, it should print a message indicating that the sum is a prime number.
"""

def add_integers(a, b):
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

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    if is_prime(result):
        print("The sum is a prime number.")