"""
QUESTION:
Create a function `algorithm(n)` that takes an integer `n` as input and returns a tuple of three values: the cumulative total of all prime numbers from 0 to `n`, the highest prime number within this range, and the lowest prime number within this range. The function should only consider positive integers within the specified range.
"""

def algorithm(n):
    def is_prime(num):
        if num <= 1:
            return False
        elif num <= 3:
            return True
        elif num%2 == 0 or num%3 == 0:
            return False
        i = 5
        while (i * i <= num):
            if (num%i == 0 or num%(i + 2) == 0):
                return False
            i = i + 6
        return True

    total = 0
    high = None
    low = None

    for i in range(n+1):
        if is_prime(i):
            total += i
            if high == None or i > high:
                high = i
            if low == None or i < low:
                low = i

    return total, high, low