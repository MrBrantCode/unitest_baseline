"""
QUESTION:
Create a function named `countPrimesRecursive` that takes an array and an index as parameters, and returns the number of prime numbers between -100 and 100 in the array. Use a recursive function and consider both positive and negative integers in the array.
"""

def is_prime(n):
    """
    Helper function to check if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def countPrimesRecursive(arr, index=0):
    if index == len(arr):
        return 0
    count = 1 if (abs(arr[index]) <= 100 and is_prime(abs(arr[index]))) else 0
    return count + countPrimesRecursive(arr, index + 1)