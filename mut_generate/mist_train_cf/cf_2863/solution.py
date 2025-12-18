"""
QUESTION:
Create a function named `countPrimesRecursive` that takes an array of integers as input and returns the count of prime numbers between -100 and 100 in the array. The function should use recursion and work with arrays containing both positive and negative integers.
"""

def is_prime(n):
    """
    Helper function to check if a number is prime.
    """
    if abs(n) < 2:
        return False
    for i in range(2, int(abs(n) ** 0.5) + 1):
        if abs(n) % i == 0:
            return False
    return True

def countPrimesRecursive(arr, index=0, count=0):
    if index == len(arr):
        return count

    if -100 <= arr[index] <= 100 and is_prime(arr[index]):
        count += 1

    return countPrimesRecursive(arr, index + 1, count)