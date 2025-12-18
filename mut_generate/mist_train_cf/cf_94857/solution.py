"""
QUESTION:
Create a function named `count_primes_in_array` that takes an array of integers as input and returns the count of prime numbers in the array that fall within the range -100 to 100. Use a for loop and an if statement in your implementation.
"""

def count_primes_in_array(arr):
    """
    This function counts the number of prime numbers in the given array within the range -100 to 100.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The count of prime numbers in the array.
    """
    count = 0
    for num in arr:
        if -100 <= num <= 100 and num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                count += 1
    return count