"""
QUESTION:
Write a function `sum_of_primes(array)` that calculates the sum of all prime numbers present in a two-dimensional array. The array may contain any number of sub-arrays, and the function should be able to process these sub-arrays recursively. The function should also include error handling for arrays that contain non-numeric values.
"""

def sum_of_primes(array):
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    try:
        sum = 0
        for i in array:
            if type(i) == list:         # if element is a list, recursion is applied
                sum += sum_of_primes(i)
            elif is_prime(i):           # if element is a prime number, add it to sum
                sum += i
        return sum
    except TypeError:                   # use error handling for non-numeric values
        print("Array should only contain numeric values.")