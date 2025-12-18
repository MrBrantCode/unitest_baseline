"""
QUESTION:
Create a function `extract_data` that takes a string as input. If the string contains a whitespace or a semicolon, return a list of substrings separated by the whitespace or semicolon. If neither exists, return the count of upper-case alphabetic characters with an even index (ord('A') = 0, ord('B') = 1, ... ord('Z') = 25) in the string.
"""

def extract_data(txt):
    if " " in txt:
        return txt.split()
    elif ";" in txt:
        return txt.split(";")
    else:
        return sum(1 for ch in txt if ch.isupper() and (ord(ch) - ord("A")) % 2 == 0)