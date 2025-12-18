"""
QUESTION:
Define a function `locate_numbers` that takes a list of integers as input and returns a sextuple (a, b, c, d, e, f). The values in the sextuple represent the following: 
- a: the smallest prime number in the list
- b: the largest prime number in the list
- c: the smallest composite number in the list
- d: the largest composite number in the list
- e: the sum of all prime numbers in the list
- f: the sum of all composite numbers in the list

If any of these criteria are not met (i.e., no prime numbers or no composite numbers in the list), the corresponding value in the sextuple should be None.
"""

# Function to check if a number is prime
def is_prime(n):
	if n < 2:
		return False
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True

# Function to check if a number is a composite
def is_composite(n):
	if n < 2:
		return False
	for i in range(2, n):
		if n % i == 0:
			return True
	return False

def locate_numbers(lst):
	if not lst:
		return (None, None, None, None, None, None)
	
	primes = []
	composites = []
	
	for n in lst:
		if is_prime(n):
			primes.append(n)
		elif is_composite(n):
			composites.append(n)
	
	a = min(primes) if primes else None
	b = max(primes) if primes else None
	c = min(composites) if composites else None
	d = max(composites) if composites else None
	e = sum(primes) if primes else None
	f = sum(composites) if composites else None
	
	return (a, b, c, d, e, f)