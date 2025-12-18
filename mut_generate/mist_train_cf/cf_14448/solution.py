"""
QUESTION:
Write a function `sum_of_primes(n)` that calculates the sum of all prime numbers from 2 to `n` with a time complexity of O(sqrt(n)). The function should take a single integer `n` as input, where `n` is a positive integer greater than or equal to 2.
"""

def sum_of_primes(n):
    """
    Calculates the sum of all prime numbers from 2 to n with a time complexity of O(sqrt(n)).
    
    Args:
    n (int): A positive integer greater than or equal to 2.
    
    Returns:
    int: The sum of all prime numbers from 2 to n.
    """
    
    # Create a boolean array isPrime[0...n] and initialize all entries to true
    isPrime = [True] * (n + 1)
    isPrime[0] = isPrime[1] = False
    
    # Initialize a variable sum to 0 to store the sum of prime numbers
    total_sum = 0
    
    # Iterate from p = 2 to sqrt(n)
    for p in range(2, int(n ** 0.5) + 1):
        # If isPrime[p] is true, then it is a prime number. Add p to sum
        if isPrime[p]:
            total_sum += p
            
            # Update all multiples of p as false in isPrime[]. Start with p*p, and increment by p for each multiple until it is less than or equal to n
            for i in range(p * p, n + 1, p):
                isPrime[i] = False
    
    # Finally, iterate from p = sqrt(n) + 1 to n
    for p in range(int(n ** 0.5) + 1, n + 1):
        # If isPrime[p] is true, then it is a prime number. Add p to sum
        if isPrime[p]:
            total_sum += p
    
    # Return sum as the sum of all prime numbers from 2 to n
    return total_sum