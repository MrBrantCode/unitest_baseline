"""
QUESTION:
Write a function `find_prime_coords` that takes a 2D array of integers as input and returns a list of coordinates (i, j) of all prime numbers in the array. The function should work with 2D arrays of any size.
"""

def find_prime_coords(array_2d):
    prime_coords = []
    for i in range(len(array_2d)):
        for j in range(len(array_2d[i])):
            num = array_2d[i][j]
            if num > 1:
                is_prime = True
                for k in range(2, int(num ** 0.5) + 1):
                    if num % k == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_coords.append((i, j))
    return prime_coords