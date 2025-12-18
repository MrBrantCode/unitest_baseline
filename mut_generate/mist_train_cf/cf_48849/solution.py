"""
QUESTION:
Create a function named `prime_multiples_count` that takes a string of logographic characters and a prime number as input. The function should count and return the number of words in the string whose lengths are multiples of the given prime number. The input string is assumed to be space-separated words.
"""

def prime_multiples_count(text, prime_num):
    text_arr = text.split()
    count = 0
    for word in text_arr:
        if len(word) % prime_num == 0:
            count += 1
    return count