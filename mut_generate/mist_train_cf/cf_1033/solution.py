"""
QUESTION:
Write a function `include_in_array` that takes an integer and its index as input. The function should return `True` if the number is a prime number, its index is a multiple of 3, the sum of its digits is divisible by 5, and the number is a palindrome.
"""

def include_in_array(num, index):
    # Check if index is a multiple of 3
    if index % 3 != 0:
        return False

    # Check if number is palindrome
    if str(num) != str(num)[::-1]:
        return False

    # Check if sum of digits is divisible by 5
    if sum(int(digit) for digit in str(num)) % 5 != 0:
        return False

    # Check if number is prime
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True