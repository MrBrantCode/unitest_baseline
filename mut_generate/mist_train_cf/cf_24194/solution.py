"""
QUESTION:
Create a function named 'get_primes' that takes an integer 'n' as input and returns a list of all prime numbers less than or equal to 'n'.
"""

def get_primes(n): 
  primes = [] 
  for num in range(2, n+1): 
    is_prime = True     
    for div in range(2, num): 
      if (num % div == 0): 
        is_prime = False      
    if is_prime: 
      primes.append(num) 
  return primes