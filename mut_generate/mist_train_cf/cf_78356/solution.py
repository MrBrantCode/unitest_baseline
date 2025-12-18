"""
QUESTION:
Write a function `isNarcissistic(n)` that takes an integer `n` and returns `True` if `n` is a Narcissistic number and `False` otherwise. A Narcissistic number is a `k`-digit number `n` where the sum of each digit raised to the power of `k` equals `n`. The input integer `n` should satisfy `1 <= n <= 10^8`.
"""

def entrance(n):
    # Convert n to string to easily get individual digits
    str_n = str(n)
    length = len(str_n)
    
    # Calculate the sum of each digit raised to the power of the length
    sum_of_powers = sum(int(num)**length for num in str_n)
    
    # Check if the sum is equal to n
    return sum_of_powers == n