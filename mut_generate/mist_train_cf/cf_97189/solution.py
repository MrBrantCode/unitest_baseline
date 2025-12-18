"""
QUESTION:
Create a function `remove_duplicates_and_primes` that takes a list of integers as input, removes duplicates and non-prime numbers, and returns a new list containing only unique prime elements. The function should iterate through each element in the input list, checking for uniqueness and primality before adding it to the output list.
"""

def remove_duplicates_and_primes(lst):
    unique_primes = []  # List to store unique prime elements
    
    for num in lst:
        # Check if the number is already encountered
        if num in unique_primes:
            continue
        
        # Check if the number is prime
        is_prime = True
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    is_prime = False
                    break
        
        # Add the number to the list if it is prime and not encountered before
        if is_prime:
            unique_primes.append(num)
    
    return unique_primes