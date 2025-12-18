"""
QUESTION:
Create a function `prime_pairs` that takes no arguments and returns two lists of positive integers, A and B, where each integer in A is paired with a corresponding integer in B. The sum of each pair must be a prime number and both integers in the pair must be greater than 10. The function should establish a one-to-one mapping between the two sets of integers, meaning each integer in A is paired with exactly one integer in B and vice versa.
"""

def is_prime(n):
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

def prime_pairs():
    A = []
    B = []
    for i in range(11, 100):  # assuming we are considering numbers up to 100
        for j in range(11, 100):
            if is_prime(i + j) and (j not in B) and (i not in A):
                A.append(i)
                B.append(j)
                break
    return A, B