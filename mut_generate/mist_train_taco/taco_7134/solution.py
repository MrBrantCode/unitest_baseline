"""
QUESTION:
Problem statement

Given the string $ S $. Find the number of all anagrams in $ S $ that are palindromic.

An anagram of the string $ X $ is an anagram of $ Y $, which means that $ X $ is equal to $ Y $, or that the rearranged characters of $ X $ are equal to $ Y $. For example, for the string abcd, abcd and cbda are anagrams, but abed, cab and abcdd are not anagrams.

When the string $ X $ is a palindrome, it means that the reverse reading of $ X $ is equal to $ X $ itself. For example, abc and ab are not palindromes, and a and abccba are palindromes.

Constraint

* $ 1 \ leq | S | \ leq 40 $ ($ | S | $ is the length of the string $ S $)
* $ S $ contains only lowercase letters.
* The answer is guaranteed to be less than $ 2 ^ {63} $.



input

Input follows the following format.


$ S $

output

Output the number on one line.

Examples

Input

ab


Output

0


Input

abba


Output

2
"""

import collections
from math import factorial

def count_palindromic_anagrams(s: str) -> int:
    # Count the frequency of each character in the string
    char_count = collections.Counter(s)
    
    # Count the number of characters with odd frequencies
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return 0  # More than one character with odd frequency means no palindromic anagram
    
    # Reduce the count of characters by 1 if they have odd frequency
    for char in char_count:
        if char_count[char] % 2 != 0:
            char_count[char] -= 1
    
    # Calculate the number of palindromic anagrams
    half_length = len(s) // 2
    permutations = factorial(half_length)
    
    for count in char_count.values():
        permutations //= factorial(count // 2)
    
    return permutations