"""
QUESTION:
Create a function `fibonacci_primes(n)` that returns a list of all prime numbers found within the first n elements of the Fibonacci progression. The function should not use any external library or resource. Additionally, develop a helper function to check for primality.
"""

def is_prime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def fibonacci_primes(n):
  def fib(n):
    if n==1:
      fibonacci = [0]
    elif n==2:
      fibonacci = [0, 1]
    else:
      fibonacci = [0, 1]
      for i in range(2, n):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return fibonacci
  
  fibonacci = fib(n)
  primes = [number for number in fibonacci if is_prime(number)]
  return primes