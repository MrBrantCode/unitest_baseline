"""
QUESTION:
Create a function named `create_prime_dictionary` that takes two parameters, `x` and `y`, where `x` is a prime number greater than 100,000 and `y` is a prime number greater than 10,000. The function should return a dictionary where each key is a unique prime number congruent to 1 modulo 4 between 100,000 and `x` (inclusive), and the value of each key is the corresponding product of the key and `y`.
"""

def create_prime_dictionary(x, y):
    prime_dict = {}

    for p in range(100000, x+1):
        if all(p % i != 0 for i in range(2, int(p**0.5)+1)):
            if p % 4 == 1:
                prime_dict[p] = p * y

    return prime_dict