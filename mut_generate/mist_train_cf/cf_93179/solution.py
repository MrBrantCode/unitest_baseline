"""
QUESTION:
Create a function `find_prime_union` that takes two arrays as input and returns an array containing the unique prime numbers from both arrays. The function should not include any duplicate values.
"""

def find_prime_union(arr1, arr2):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = set()
    for num in arr1 + arr2:
        if is_prime(num):
            result.add(num)
    return list(result)