"""
QUESTION:
Write a function `sum_of_squares` that takes an array of integers as input and returns a list of numbers that can be expressed as the sum of two squares where the sum is also a prime number. The function should consider all possible pairs of squares that sum up to each number in the array and check if the sum is prime.
"""

def sum_of_squares(arr):
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

    result = []
    for num in arr:
        for i in range(int(num**0.5) + 1):
            j = int((num - i**2)**0.5)
            if i**2 + j**2 == num and is_prime(i**2 + j**2):
                result.append(num)
                break
    return result