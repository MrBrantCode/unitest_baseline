"""
QUESTION:
Implement a function `analyze_string_complex(s)` that takes a string `s` as input and returns different results based on the presence of commas or colons. If `s` contains at least one comma or colon, return a list of words separated by commas or colons and a list of indices where these punctuations are found. If `s` does not contain commas or colons, return the count of lowercase letters with odd indices (where 'a' is 0, 'b' is 1, ..., 'z' is 25) and a list of their positions.
"""

def analyze_string_complex(s):
    punctuation_positions = [i for i, char in enumerate(s) if char in [',', ':']]
    if punctuation_positions:
        return [word for word in s.replace(',', ':').split(':')], punctuation_positions
    else:
        odd_letters_positions = [i for i, char in enumerate(s) if char.islower() and (ord(char) - ord('a')) % 2 != 0]
        return len(odd_letters_positions), odd_letters_positions