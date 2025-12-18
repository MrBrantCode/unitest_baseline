"""
QUESTION:
Create a function named `palindrome_prime` that takes an integer `max_num` as input and returns a list of tuples. Each tuple should contain a palindrome prime number less than or equal to `max_num` and its digit sum. If `max_num` is not a positive integer, the function should return an empty list. If `max_num` is a decimal number, the function should ignore the decimal part and treat it as an integer.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def sum_digits(n):
    return sum(int(digit) for digit in str(n))

def palindrome_prime(max_num):
    if max_num <= 0:
        return []
    max_num = int(max_num)
    
    result = []
    for num in range(2, max_num + 1):
        if is_prime(num) and is_palindrome(num):
            result.append((num, sum_digits(num)))
    
    return result