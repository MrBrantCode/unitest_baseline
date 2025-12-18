"""
QUESTION:
Write a function `is_pleasant(s)` that determines if a given string `s` is pleasant. A string is pleasant if its length is at least 4, every 4 consecutive letters are distinct, every distinct letter appears at least twice, there are no identical letters next to each other, and the sum of the occurrences of each distinct letter is a prime number.
"""

import collections
import math

def is_pleasant(s):
    # function to check prime number
    def is_prime(n):
        if n<2 or (n>2 and n%2==0):
            return False
        for i in range(3,int(math.sqrt(n))+1,2):
            if n%i==0:
               return False
        return True

    # length guard clause
    if len(s) < 4:
        return False

    letter_frequencies = collections.Counter(s)

    # distinct letters appears at least twice
    for freq in letter_frequencies.values():
        if freq < 2 or not is_prime(freq):
            return False

    # check every four consecutive letters are distinct
    queue = collections.deque(maxlen=4)
    for letter in s:
        if letter in queue:
            return False
        queue.append(letter)

    # check no identical letters next to each other
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False

    return True