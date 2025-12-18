"""
QUESTION:
Design a function named `twinPrimePairs` that takes two integers `start` and `end` as input, where `start` is inclusive and `end` is exclusive. The function should identify and print all the twin prime pairs within the given range. A twin prime pair is a pair of prime numbers that are two apart.
"""

def twinPrimePairs(start, end):
    def isPrime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    for i in range(start, end):
        j = i + 2
        if j < end and isPrime(i) and isPrime(j):
            print("{0} and {1}".format(i, j))