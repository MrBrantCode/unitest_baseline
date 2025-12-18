"""
QUESTION:
Create a function `find_primes(lst)` that takes a list of integers as input. The function should return a list of prime numbers from the input list, with duplicates removed and in ascending order. The function should have a time complexity of O(n).
"""

def find_primes(lst):
    # Remove duplicates
    lst = list(set(lst))
    
    # Initialize an empty list to store prime numbers
    primes = []
    
    # Iterate over each number in the list
    for num in lst:
        # Check if the number is greater than 1
        if num > 1:
            # Iterate from 2 to the square root of the number (inclusive)
            for i in range(2, int(num ** 0.5) + 1):
                # Check if the number is divisible by any other number
                if num % i == 0:
                    break
            else:
                # If the loop completes without finding a divisor, the number is prime
                primes.append(num)
    
    # Sort the prime numbers in ascending order
    primes.sort()
    
    return primes