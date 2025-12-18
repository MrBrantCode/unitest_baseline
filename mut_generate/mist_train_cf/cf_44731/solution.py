"""
QUESTION:
Create a function called `possible_palindrome` that takes a string of alphanumeric characters as input and returns a tuple containing a boolean indicating whether the string can form a palindrome and a string representing one possible palindrome if it can be formed. The returned palindrome should be at least 3 characters long and unique. If the string cannot form a palindrome, the function should return a boolean `False` and `None` for the palindrome.
"""

from collections import Counter

def possible_palindrome(string):
    # count frequency of each character
    frequency = Counter(string)

    # count how many characters have an odd frequency
    odd_freq = [v % 2 for v in frequency.values()]
    odd_freq_count = sum(odd_freq)

    # string can form palindrome if and only if the number of odd frequency character <= 1
    if odd_freq_count > 1:
        return False, None

    odd_char = [k for k,v in frequency.items() if v%2==1]
    half_palindrome = ''.join([k*(v//2) for k, v in frequency.items()])

    if odd_char:
        half_palindrome += odd_char[0]

    palindrome = half_palindrome + half_palindrome[::-1]
    
    if len(palindrome) < 3:
        return False, None

    return True, palindrome