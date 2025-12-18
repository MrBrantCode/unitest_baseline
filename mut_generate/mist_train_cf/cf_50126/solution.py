"""
QUESTION:
Write a function `leetspeak(s)` that takes a string `s` as input and returns its leetspeak equivalent. The function should replace the following characters with their corresponding leetspeak characters: A with 4, B with 8, E with 3, G with 6, I with 1, O with 0, S with 5, and T with 7. The function should be case-insensitive and leave characters without leetspeak equivalents unchanged.
"""

def leetspeak(s):
    leet_map = {'A': '4', 'B': '8', 'E': '3', 'G': '6', 'I': '1', 'O': '0', 'S': '5', 'T': '7'}
    return ''.join(leet_map[i.upper()] if i.upper() in leet_map else i for i in s)