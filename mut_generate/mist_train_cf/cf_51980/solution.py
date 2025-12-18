"""
QUESTION:
Compute the sum of the first four instances of 'engineers' paradises', where an 'engineers' paradise' is defined as an integer n such that: 
- (n-9, n-3), (n-3,n+3), (n+3, n+9) form a triple-pair of sexy prime numbers (consecutive pairs of prime numbers with a difference of 6), 
- and the integers n-8, n-4, n, n+4, n+8 are all practical numbers (where a practical number is an integer n such that every integer from 1 to n can be represented as a sum of unique divisors of n).
"""

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True  

def is_practical(n):
    if n == 1: return True
    if n != 2 and n % 2 != 0: return False
    d = [1, 2]
    sum_d = 3
    limit = n / 2
    for i in range(4, int(n / sum_d) + 1, 2):
        if n % i == 0:
            if i > sum_d + 1: return False
            d.append(i)
            sum_d += i
            if i > limit: return True
    return False

def sexy(n):
    return is_prime(n) and is_prime(n+6)

def triple_pair(n):
    return sexy(n-9) and sexy(n-3) and sexy(n+3)

def entance():
    rangelimit = 20000
    paradises = []
    for n in range(23, rangelimit):
        if triple_pair(n) and is_practical(n-8) and is_practical(n-4) and is_practical(n) and is_practical(n+4) and is_practical(n+8):
            paradises.append(n)
            if len(paradises) == 4:
                break
    return sum(paradises)