"""
QUESTION:
Write a function `is_perfect(num)` that checks if a number is perfect, considering both positive and negative integers, as well as floating point numbers. A number is perfect if its sum of divisors (excluding itself) is equal to its absolute value. The function should account for exceptions and potential errors, and handle cases where the input is not a valid number.
"""

def is_perfect(num):
    try:
        num = abs(int(num))  # Convert the number to a positive integer
    except ValueError:  # Catch exceptions for invalid inputs e.g. strings
        return "Invalid input"

    if num == 0:  # Special case
        return False

    divisor_sum = 1
    for i in range(2, int(num ** 0.5) + 1):  # Check up to the square root of the number for efficiency
        if num % i == 0:  # i is a divisor
            if num / i == i:  # If the divisor and the quotient are the same, add it once
                divisor_sum += i
            else:  # Otherwise, add both the divisor and the quotient
                divisor_sum += i
                divisor_sum += num // i

    if divisor_sum == num:
        return "Positive perfect number"
    elif divisor_sum == -num:
        return "Negative perfect number"
    else:
        return False