"""
QUESTION:
Generate a function called `lucas_sequence(n)` that generates the Lucas sequence up to 'n' numbers. The Lucas sequence is a series of numbers where each number is the sum of the two preceding numbers, starting with the first two prime numbers (2 and 3). The function should use memoization to store previously calculated values and achieve a time complexity of O(n).
"""

def lucas_sequence(n):
    primes = [2, 3]  

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(4, n+1):
        if is_prime(i):
            primes.append(i)

    memo = {}
    def lucas(num):
        if num == 0:
            return primes[0]
        if num == 1:
            return primes[1]
        if num in memo:
            return memo[num]
        else:
            memo[num] = lucas(num-1) + lucas(num-2)
            return memo[num]

    lucas_seq = []
    for i in range(n):
        lucas_seq.append(lucas(i))
    return lucas_seq