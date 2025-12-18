"""
QUESTION:
Write a function `average_of_primes` that calculates the average of all prime numbers in a given array. If the array does not contain any prime numbers, the function should return -1.0. 

The function should take an array of integers as input and return a float value. The array may contain duplicate numbers and/or negative numbers. Prime numbers are natural numbers greater than 1 that have no positive divisors other than 1 and themselves.
"""

def average_of_primes(arr):
    """
    This function calculates the average of all prime numbers in a given array.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    float: The average of all prime numbers in the array. If the array does not contain any prime numbers, returns -1.0.
    """

    # Initialize an empty list to store prime numbers
    prime_numbers = []
    
    # Iterate over each number in the array
    for num in arr:
        # Check if the number is greater than 1
        if num > 1:
            # Assume the number is prime
            is_prime = True
            
            # Check for divisors from 2 to the square root of the number
            for i in range(2, int(num ** 0.5) + 1):
                # If the number is divisible by any of these, it's not prime
                if num % i == 0:
                    is_prime = False
                    break
            
            # If the number is prime, add it to the list
            if is_prime:
                prime_numbers.append(num)
    
    # If no prime numbers were found, return -1.0
    if len(prime_numbers) == 0:
        return -1.0
    # Otherwise, return the average of the prime numbers
    else:
        return sum(prime_numbers) / len(prime_numbers)