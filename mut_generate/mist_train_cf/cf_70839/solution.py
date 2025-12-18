"""
QUESTION:
Design a function named `main` that takes two integer parameters `lower` and `upper`, representing a range. The function should generate all prime numbers within this range and identify the prime numbers that can be expressed as the sum of consecutive prime numbers with the most elements. The function should print the sequence of all prime numbers within the given range, and for each identifiable prime number, print the prime number itself and the sequence of consecutive prime numbers that sum up to it.
"""

def entrance(lower, upper):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_primes(lower, upper):
        primes = []
        for num in range(lower, upper+1):
            if is_prime(num):
                primes.append(num)
        return primes

    def find_consecutive_primes(primes):
        max_length = 0
        max_prime = 0
        max_sequence = []
        for i in range(len(primes)):
            sum_of_primes = primes[i]
            for j in range(i + 1, len(primes)):
                sum_of_primes += primes[j]
                if sum_of_primes in primes:
                    length = j - i + 1
                    if length > max_length:
                        max_length = length
                        max_prime = sum_of_primes
                        max_sequence = primes[i:j+1]
        yield (max_prime, max_sequence)

    primes = generate_primes(lower, upper)
    results = list(find_consecutive_primes(primes))
    
    print("All prime numbers between {} and {} are: ".format(lower, upper))
    print(primes)
    
    if results:
        print('\nThe prime that can be expressed as the sum of most consecutive primes:')
        for prime, consecutive_primes in results:
            print("{} can be expressed as the sum of these consecutive primes: {}".format(prime, consecutive_primes))
    else:
        print('\nNo prime can be expressed as the sum of consecutive primes.')