"""
QUESTION:
Given an array of integers, write a function `multiply_by_next_prime` that multiplies each element by the smallest prime number greater than 3. If any element in the array is divisible by the smallest prime number greater than 3, replace that element with the next prime number greater than 3 before multiplying. The function should return the new array.
"""

def multiply_by_next_prime(arr):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def next_prime(n):
        while True:
            n += 1
            if is_prime(n):
                return n

    prime = 5  # Start with the smallest prime greater than 3
    result = []
    for num in arr:
        if num % prime == 0:
            prime = next_prime(prime)
        result.append(num * prime)
    return result