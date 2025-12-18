"""
QUESTION:
Implement the function `distinctive_elements(sequence)` that takes a non-empty array of positive integers as input and returns all unique integers satisfying the following conditions:
- The frequency of the integer in the array surpasses half of the integer's value.
- The frequency is a prime number.
- The input array replicates an ascending Fibonacci sequence pattern.

The function should return an empty array if no numbers meet these conditions.
"""

from collections import Counter

def distinctive_elements(sequence):
    '''
    This function receives a non-empty array of positive integers and returns all unique integers satisfying the given conditions.
    '''

    # check if the sequence is a fibonacci sequence
    fib_seq = [0, 1]
    while fib_seq[-1] < max(sequence):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    if sorted(list(set(sequence))) != fib_seq[1:len(set(sequence))+1]:
        return []

    # calculate the frequencies of the elements
    counts = Counter(sequence)

    def is_prime(n):
        """return True if number is prime"""
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # find distinctive elements
    distinct = [k for k, v in counts.items() if v > k / 2 and is_prime(v)]

    return sorted(distinct)