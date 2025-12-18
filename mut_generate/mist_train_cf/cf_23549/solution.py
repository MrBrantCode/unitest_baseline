"""
QUESTION:
Create a function `prime_nums` that takes an integer `n` as input and returns a list of all prime numbers from 2 to `n`. The function should consider a prime number as a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def prime_nums(n): 
    prime_list = [] 
    for i in range(2, n + 1): 
        for j in range(2,i): 
            if (i % j) == 0: 
                break
        else: 
            prime_list.append(i)
    return prime_list