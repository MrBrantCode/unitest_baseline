"""
QUESTION:
Write a function named `insert_character` that takes a string and a character as input and returns a new string where the given character is inserted at every prime index in the original string. The index is considered prime if its 0-based position in the string is a prime number.
"""

def insert_character(string, character):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_indexes = [i for i in range(len(string)) if is_prime(i)]
    for index in prime_indexes:
        string = string[:index] + character + string[index:]
    return string