"""
QUESTION:
Write a function `last_ten_digits_of_series(max_digits)` that takes an integer `max_digits` as input and returns the last ten digits of the sum of the series 1^1 + 2^2 + 3^3 + ... + max_digits^max_digits. Ensure the function can handle large values of `max_digits` efficiently and the input integer `max_digits` is greater than 0.
"""

def last_ten_digits_of_series(max_digits):
    sum = 0
    for i in range(1, max_digits+1):
        sum += pow(i, i, 10**10)  # Using modular exponentiation to efficiently calculate last ten digits
    return str(sum)[-10:]