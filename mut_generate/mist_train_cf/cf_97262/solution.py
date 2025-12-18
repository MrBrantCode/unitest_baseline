"""
QUESTION:
Implement a function `find_last_element` that takes a list of integers as input and returns the last element if it is prime, or the nearest smaller prime number if the last element is not prime. The function should also check for and report the following conditions: 

- If the input list is empty.
- If the input list contains duplicate elements.

The function should return a message indicating the condition if either of the above conditions is met, and should return the prime number as an integer if the last element or the nearest smaller prime number is found.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_last_element(lst):
    if len(lst) == 0:
        return "The list is empty."
    if len(lst) != len(set(lst)):
        return "The list contains duplicate elements."
    last_element = lst[-1]
    if is_prime(last_element):
        return last_element
    else:
        for i in range(last_element - 1, 1, -1):
            if is_prime(i):
                return i