"""
QUESTION:
Write a function called `generate_dict` that takes a list of integers as input and returns a dictionary. The keys of the dictionary should be the integers of the list at prime index positions and the values should be their corresponding squares. The list must contain at least two unique integers. The function should return an error message if the list has less than two elements.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_dict(lst):
    if len(lst) < 2:
        return "List must contain at least two integers"
    return {v: v**2 for i, v in enumerate(lst) if is_prime(i)}