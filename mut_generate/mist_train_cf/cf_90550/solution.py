"""
QUESTION:
Create a function called `prime_factorial` that takes a dictionary `data` as input and returns a new dictionary. The new dictionary should only include key-value pairs from the input dictionary where the key is a prime number. For each included key-value pair, the value should be replaced with the factorial of the original value. Implement a recursive function called `factorial` to calculate the factorial.
"""

def prime_factorial(data):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n-1)

    return {k: factorial(v) for k, v in data.items() if k > 1 and all(k % i != 0 for i in range(2, int(k**0.5) + 1))}