"""
QUESTION:
Create a function called `transpose` that takes a sequence of integers as input. The function should return a new sequence where each individual element is replaced by its square root if the square root is a prime number, otherwise replace the number with its cubic root. The input sequence contains only positive integers and the output should be a list of floats.
"""

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

def transpose(seq):
    result = []
    for num in seq:
        root = num ** 0.5
        if root.is_integer() and is_prime(int(root)):
            result.append(root)
        else:
            result.append(num ** (1/3.0))
    return result