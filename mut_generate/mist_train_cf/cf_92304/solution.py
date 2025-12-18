"""
QUESTION:
Create a function called `find_second_highest_prime` that takes a list of integers as input and returns the second highest prime number in the list. The function should return `None` if there are less than two prime numbers in the list.
"""

def find_second_highest_prime(numbers):
    primes = []
    
    for num in numbers:
        if num > 1:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    
    primes.sort(reverse=True)
    if len(primes) >= 2:
        return primes[1]
    else:
        return None