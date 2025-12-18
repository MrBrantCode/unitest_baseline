"""
QUESTION:
Write a function `multiply(lst)` that takes a list of integers `lst` of length between 200 and 1000 (inclusive) and returns the product of all odd elements at even indices that are divisible by 3 and have a prime number immediately following them in the list, excluding the last number. If no such elements are found, the function should return -1 (or any other specified value). The function should be efficient for large inputs.
"""

def multiply(lst):
    def isPrime(n):
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

    product = 1
    found = False

    for i in range(len(lst) - 1):
        if i % 2 == 0 and lst[i] % 2 != 0 and lst[i] % 3 == 0 and isPrime(lst[i + 1]):
            product *= lst[i]
            found = True
            
    if found: 
        return product
    else: 
        return -1  