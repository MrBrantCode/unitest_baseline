"""
QUESTION:
Create a function named "create_prime_array" that takes an integer "n" as input and returns an array of length "n" filled with prime numbers starting from 3. The generated array should exclude often repeated "twin prime numbers" where the difference between the last two elements in the array and the next prime number is 2. The input "n" should be in the range of 5 to 15 inclusive, otherwise, return an error message.
"""

def create_prime_array(n):
    if n < 5 or n > 15:
        return "Error: Input 'n' should be in range 5-15 inclusive"
    primes = []
    i = 3
    while len(primes) < n:
        
        for p in primes:
            if i % p == 0:
                break
        else:
            if len(primes) >= 2 and primes[-1] - primes[-2] == 2 and i - primes[-1] == 2:
                i += 2
                continue
            primes.append(i)
            
        i += 2
    return primes