"""
QUESTION:
Create a function named `generate_array` that generates a two-dimensional array. The array should contain the squared outcomes of the first n odd prime digit integers in ascending order, where each row has an increasing sequence from left to right. The function should take an integer n as input and optimize for both time and space complexity.
"""

def generate_array(n):
    primes = [2]
    num = 3
    while len(primes) < n:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
        num += 2
    return [[x ** 2 for x in primes[i:]] for i in range(n)]