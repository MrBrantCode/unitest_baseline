"""
QUESTION:
Write a function named `sum_of_integers` that takes a list of strings, where each string represents a positive integer. The function should convert these strings to integers, remove any duplicates, calculate their sum, and check if the sum is a prime number. Return True if the sum is prime, and False otherwise.
"""

def sum_of_integers(lst):
    # Convert strings to integers and remove duplicates
    integers = list(set(map(int, lst)))
    
    # Calculate the sum
    total = sum(integers)
    
    # Check if the sum is a prime number
    if total < 2:
        return False
    for i in range(2, int(total ** 0.5) + 1):
        if total % i == 0:
            return False
    return True