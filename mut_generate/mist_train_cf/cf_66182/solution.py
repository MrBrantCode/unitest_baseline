"""
QUESTION:
Create a function named `prime_odd_numbers` that takes a list of integers as input. The function should return a tuple of two distinct prime odd numbers from the list whose sum is divisible by 5, or None if no such pair exists. Assume the input list contains only positive integers.
"""

def prime_odd_numbers(catalog):
    # Function to check if a number is prime
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))
      
    # Filter the list to contain only prime odd numbers
    prime_odds = [num for num in catalog if num % 2 != 0 and is_prime(num)]
    
    # Loop over every unique pair of numbers in the list
    for i in range(len(prime_odds)):
        for j in range(i + 1, len(prime_odds)):
            # Check if the sum of the pair is divisible by 5
            if (prime_odds[i] + prime_odds[j]) % 5 == 0:
                return (prime_odds[i], prime_odds[j]) # Returning the pair of numbers
    return None # If no such pair found