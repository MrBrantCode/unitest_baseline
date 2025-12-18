"""
QUESTION:
Write a function `delete_items(lst)` that takes a list of integers as input, removes all items whose value is divisible by 3 and greater than 10, and also removes any items that are prime numbers. Return the updated list.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def delete_items(lst):
    for item in lst[:]:
        if item % 3 == 0 and item > 10:
            lst.remove(item)
        elif is_prime(item):
            lst.remove(item)
    return lst