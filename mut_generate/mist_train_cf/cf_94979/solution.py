"""
QUESTION:
Write a function `get_prime_chars(stringA, stringB)` that takes two strings as input and returns a list of characters. The function should only consider characters from `stringA` with ASCII values greater than 100 and include a character in the output list if its ASCII value is a prime number. The function can ignore `stringB`.
"""

def get_prime_chars(stringA, stringB):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_chars = []
    for char in stringA:
        if ord(char) > 100 and is_prime(ord(char)):
            prime_chars.append(char)

    return prime_chars