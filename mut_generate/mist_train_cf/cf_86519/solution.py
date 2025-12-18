"""
QUESTION:
Write a function `delete_items(lst)` that takes a list of integers `lst` as input. The function should delete all items in the list whose value is either divisible by both 3 and 5 and greater than 10, or a prime number.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def delete_items(lst):
    i = 0
    while i < len(lst):
        if (lst[i] % 3 == 0 and lst[i] % 5 == 0 and lst[i] > 10) or is_prime(lst[i]):
            del lst[i]
        else:
            i += 1