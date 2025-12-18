"""
QUESTION:
Create a function `process_3d_array(arr)` that takes a 3D array `arr` as input. The function should iterate over each element in the array and assign 1 to the element if it is divisible by a prime number. The function should use a helper function `is_prime(n)` that checks whether a given number `n` is prime. The `is_prime(n)` function should return `True` if `n` is prime and `False` otherwise.
"""

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def process_3d_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            for k in range(len(arr[0][0])):
                if arr[i][j][k] % 2 == 0 or any(arr[i][j][k] % p == 0 for p in range(3, int(arr[i][j][k]**0.5) + 1, 2)):
                    if is_prime(arr[i][j][k]) or any(is_prime(p) for p in range(2, int(arr[i][j][k]**0.5) + 1)):
                        arr[i][j][k] = 1
    return arr