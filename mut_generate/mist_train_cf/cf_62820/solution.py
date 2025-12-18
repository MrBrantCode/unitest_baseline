"""
QUESTION:
Create a function called `solve` that takes a list of integers as input. The function should return a dictionary where each key is a unique even prime number from the input list and each value is the cumulative product of its occurrences. If a number is not prime or not even, it should be excluded from the dictionary.
"""

from collections import Counter

def solve(arr):
    prime_product = {}
    even_product = 1 
    counter = Counter(arr)
    for no in counter:
        if no > 1 and all(no%i != 0 for i in range(2, int(no**0.5) + 1)):
            if no % 2 == 0:
                for _ in range(counter[no]):
                    even_product *= no
                prime_product[no] = even_product
                even_product = 1
    return prime_product