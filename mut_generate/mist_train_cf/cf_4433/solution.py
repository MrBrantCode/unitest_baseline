"""
QUESTION:
Implement a function called `delete_primes` that takes two parameters: `arr` (an array of integers) and `n` (a number). The function should delete all the prime numbers in the first `n` numbers of the array and return the modified array. Assume that `arr` and `n` are valid inputs. Do not use any built-in functions or libraries to check for prime numbers. The function should handle edge cases, such as when `n` is less than or equal to 0, or when the array is empty.
"""

def delete_primes(arr, n):
    if n <= 0 or len(arr) == 0:
        return arr

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [arr[i] for i in range(min(n, len(arr))) if is_prime(arr[i])]
    return [x for x in arr if x not in primes]