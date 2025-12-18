"""
QUESTION:
Create a function named `find_last_element` that takes a list of integers as input and outputs the last element if it is prime, or the nearest prime number smaller than the last element if it is not. The function should first check if the list is empty and output "The list is empty." if so. If the list contains any duplicate elements, the function should output "The list contains duplicate elements." and not proceed with finding the last element.
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