"""
QUESTION:
Create a function `check_integer_properties(n)` that takes an integer `n` as input. The function should return a string indicating whether the number is odd or even, and whether it is a prime number. If the input is not an integer, the function should return an error message "Error: Input is not an integer". If the input is less than or equal to 0, the function should return an error message "Error: Input should be greater than 0".
"""

def check_integer_properties(n):
    # Check if input is an integer
    try:
        n = int(n)
    except ValueError:
        return "Error: Input is not an integer"

    # Check if input is odd or even
    if n % 2 == 0:
        odd_or_even = "Even"
    else:
        odd_or_even = "Odd"

    # Check if input is prime
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                is_prime = "No"
                break
        else:
            is_prime = "Yes"
    elif n == 1:
        is_prime = "No"
    else:
        return "Error: Input should be greater than 0"

    return "{0} is an {1} number and it is {2} a prime number".format(n, odd_or_even, "not" if is_prime == 'No' else '')