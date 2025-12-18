"""
QUESTION:
Design a function called `logogram_prime_factor` that takes two parameters: a string of logograms and a prime number. The function should determine the amount of logograms from the input string that have a length in factors of the prime number. The input string should be split into words (logograms) using spaces as delimiters. The function should count the number of logograms where the length of the word is a multiple of the given prime number and return this count.
"""

def logogram_prime_factor(logogram_string, prime_number):
    logograms = logogram_string.split()
    count = 0
    for logogram in logograms:
        if len(logogram) % prime_number == 0: 
            count += 1
    return count