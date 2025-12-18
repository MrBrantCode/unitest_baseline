"""
QUESTION:
Write a function named "print_prime_index_consonants" that takes a string as input and prints every lowercase consonant in the reversed string at a prime index. A prime index is an index that is a prime number. Only consider the letters in the reversed string, and ignore non-alphabetic characters, uppercase letters, and vowels.
"""

def print_prime_index_consonants(s):
    """
    Prints every lowercase consonant in the reversed string at a prime index.

    Args:
    s (str): The input string.
    """

    def is_prime(n):
        """
        Checks if a number is prime.

        Args:
        n (int): The number to check.

        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    reversed_string = s[::-1]
    for index, letter in enumerate(reversed_string):
        if letter.isalpha() and letter.islower() and letter not in ['a', 'e', 'i', 'o', 'u'] and is_prime(index):
            print(letter)