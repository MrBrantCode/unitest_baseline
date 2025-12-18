"""
QUESTION:
Write a function named `last_element` that takes a list of integers as input. If the list is empty, return the string 'The list is empty.' Otherwise, if the last element of the list is a prime number, return the last element itself; otherwise, return the nearest prime number that is smaller than the last element.
"""

def last_element(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_previous_prime(n):
        while True:
            n -= 1
            if is_prime(n):
                return n

    if len(lst) == 0:
        return "The list is empty."
    else:
        last = lst[-1]
        if is_prime(last):
            return last
        else:
            return find_previous_prime(last)