"""
QUESTION:
Function `permutation` and `count` variable are given, calculate the number of palindromic arrangements that can be constructed using the letters in the word MISSISSIPPI, with a length of at least 2 and at most 11, that contain at least one 'M'. The count variable contains the frequency of each letter in the word MISSISSIPPI: {'M': 1, 'I': 4, 'S': 4, 'P': 2}.
"""

import math

def count_palindromes(count):
    # total palindromes (with and without M)
    total = sum(math.factorial(sum(count.values())//2) // (math.factorial(sum(count.values())//2 - count[letter]//2) * math.factorial(count[letter]//2)) for letter in count)

    # palindromes without M
    without_M = sum(math.factorial((sum(count.values())-1)//2) // (math.factorial((sum(count.values())-1)//2 - count[letter]//2) * math.factorial(count[letter]//2)) for letter in count if letter != 'M')

    # palindromes with M
    with_M = total - without_M

    return with_M