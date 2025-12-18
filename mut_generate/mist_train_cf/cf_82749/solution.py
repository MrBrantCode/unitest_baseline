"""
QUESTION:
Create a function called `prime_matrix()` that generates a 5x5 square matrix filled with prime numbers in sequential order, starting from the smallest prime number 2. The function should return a 2D list where each element is a prime number.
"""

def is_prime(n):
    """Function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_matrix():
    """Function to generate a 5x5 matrix filled with sequential prime numbers"""
    matrix = []
    prim_count = 0
    num = 2
    while prim_count < 25:
        if is_prime(num):
            if prim_count % 5 == 0:
                matrix.append([])
            matrix[prim_count // 5].append(num)
            prim_count += 1
        num += 1
    return matrix