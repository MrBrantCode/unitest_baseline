"""
QUESTION:
Write a function `fragment_counter` that takes a string as input and returns the number of fragments in the string. A fragment is defined as a sequence of consecutive alphabetic characters that are separated by whitespace, punctuation, or a digit. Ignore any leading or trailing whitespace, punctuation, or digits.
"""

def fragment_counter(s):
    s = s.strip(' .,;:"\'?!1234567890')
    fragment_count = 0
    in_fragment = False
    for char in s:
        if char.isalpha():
            if not in_fragment:
                fragment_count += 1
                in_fragment = True
        else:
            in_fragment = False
    return fragment_count