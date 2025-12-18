"""
QUESTION:
Write a function `sum_positive_even(array)` that returns the sum of the positive even elements of a given array, excluding any elements that are either divisible by 3 and are prime numbers or divisible by both 2 and 5 but not by 7.
"""

def sum_positive_even(array):
    # Initialize a variable to store the sum
    total = 0
    
    # Function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Iterate through each element in the array
    for num in array:
        # Check if the number is positive and even
        if num > 0 and num % 2 == 0:
            # Check if the number is divisible by 3 and is a prime number
            if num % 3 != 0 or not is_prime(num):
                # Check if the number is divisible by 2 and 5, and not divisible by 7
                if not (num % 2 == 0 and num % 5 == 0 and num % 7 != 0):
                    # Add the number to the sum
                    total += num
    
    return total