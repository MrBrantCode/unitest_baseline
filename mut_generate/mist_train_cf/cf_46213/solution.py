"""
QUESTION:
Write a function `third_smallest_prime_in_range` that takes two integers `start` and `end` as input and returns the third smallest prime number within the range exclusive. If the range does not contain at least three prime numbers, return a message indicating this.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while(i * i <= n):
        if (n%i == 0 or n%(i + 2) == 0):
            return False
        i += 6
    return True

def third_smallest_prime_in_range(start, end):
    prime_count = 0
    for i in range(start+1, end):  
        if is_prime(i):
            prime_count += 1
            if prime_count == 3:  
                return i
    return "There are less than 3 prime numbers in the range."