"""
QUESTION:
Create a function named `sum_of_primes` that takes a list of integers as input. The function should calculate the sum of all prime numbers in the list and append this sum to the end of the list. The function should return the modified list. Assume that the input list contains only integers and does not need to be validated.
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