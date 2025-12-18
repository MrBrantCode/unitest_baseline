"""
QUESTION:
Write a function called `calc_percentage` that takes a list of integers as input and returns the percentage of numbers in the list that are both prime and greater than 5. The function should return the result as a string in the format 'xx.xx%'. Assume that the input list is not empty.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i**2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def calc_percentage(nums):
    count = sum(1 for num in nums if num > 5 and is_prime(num))
    return f'{(count / len(nums)) * 100:.2f}%' 