"""
QUESTION:
Create a function `find_prime_numbers(n)` that takes an integer `n` as input and returns two lists: one containing all prime numbers up to `n` and another containing the count of each prime number. The function should not include 0 and 1 in the list of prime numbers and the counts should be based on the number of times each prime number occurs in the range from 2 to `n`.
"""

def find_prime_numbers(n):
    primes = [] 
    prime_counts = [] 
    
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(num)
            prime_counts.append(1) 
        else:
            if num in primes:
                prime_index = primes.index(num)
                prime_counts[prime_index] += 1 
    
    return primes, prime_counts