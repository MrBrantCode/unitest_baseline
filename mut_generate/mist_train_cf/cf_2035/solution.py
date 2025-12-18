"""
QUESTION:
Create a function named `sum_of_primes` that takes a list of integers as input. The function should find the sum of all prime numbers in the list and append this sum to the end of the list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should return the modified list.
"""

def sum_of_primes(numbers):
    primes = []
    for num in numbers:
        if num > 1:
            is_prime = True
            for i in range(2, int(num/2) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    
    sum_of_primes = sum(primes)
    numbers.append(sum_of_primes)
    
    return numbers