"""
QUESTION:
Write a function named `sum_and_average_primes` that takes a positive integer n greater than 2 as input, returns the sum of all prime numbers up to n, and prints the prime numbers in ascending order and their average.
"""

def sum_and_average_primes(n):
    """
    This function calculates the sum of all prime numbers up to n,
    prints the prime numbers in ascending order, and prints their average.

    Args:
        n (int): A positive integer greater than 2.

    Returns:
        int: The sum of all prime numbers up to n.
    """

    # Initialize a list to store prime numbers
    primes = []

    # Iterate over all numbers from 2 to n (inclusive)
    for possiblePrime in range(2, n + 1):
        
        # Assume number is prime until shown it is not.
        isPrime = True
        
        # Iterate from 2 to the square root of the possible prime number
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            
            # If the possible prime number is divisible by any of these values, it's not prime
            if possiblePrime % num == 0:
                isPrime = False
                break
        
        # If the number is still marked as prime, add it to the list of primes
        if isPrime:
            primes.append(possiblePrime)

    # Calculate the sum of prime numbers
    sum_of_primes = sum(primes)

    # Print the prime numbers in ascending order
    print("The prime numbers up to", n, "are:", ', '.join(map(str, primes)))

    # Calculate and print the average of prime numbers
    average_of_primes = sum_of_primes / len(primes)
    print("The sum of all prime numbers up to", n, "is", sum_of_primes)
    print("The average of the prime numbers up to", n, "is", round(average_of_primes, 4))
    
    return sum_of_primes