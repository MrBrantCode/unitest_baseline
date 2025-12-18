"""
QUESTION:
Create a function `fib_lower_vowel_count(s)` that calculates the frequency of lowercase vowels at Fibonacci-indexed characters in a string `s`. The string `s` must be no more than 2000 characters long. The function should return the count of lowercase vowels at Fibonacci-indexed positions in the string.
"""

def fib_lower_vowel_count(s):
    vowels = 'aeiou'
    count = 0
    a, b = 0, 1  # Initial Fibonacci numbers
    for i, c in enumerate(s):
        if i == b:
            if c in vowels:
                count += 1
            a, b = b, a + b  # Move to next Fibonacci numbers
        if b > len(s):  # Early stop if next Fibonacci number is larger than string length
            break
    return count