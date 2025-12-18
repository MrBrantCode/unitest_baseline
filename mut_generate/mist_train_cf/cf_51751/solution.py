"""
QUESTION:
Create a function called `fib_lower_vowel_count(s)` that takes a string `s` with a maximum length of 2000 characters. Calculate the number of lower-case vowel letters at the Fibonacci indexes of the string. Return the count of lower-case vowels at these indexes.
"""

def fib_lower_vowel_count(s):
    
    def fibonacci(max_index):
        """Function to generate Fibonacci numbers upto given index"""
        fib_seq = [0, 1]
        while fib_seq[-1] < max_index:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

    fib_indexes = fibonacci(len(s))
    lower_vowel = 'aeiou'
    vowel_count = 0

    for i in fib_indexes:
        if i < len(s) and s[i] in lower_vowel:
            vowel_count += 1

    return vowel_count