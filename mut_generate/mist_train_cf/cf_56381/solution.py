"""
QUESTION:
Write a function `find_longest_run(s)` that takes an encoded string `s` as input, where each character is followed by its frequency. The function should return the character with the longest run. If there are two characters with the same longest run length, the function should return the character that appears first. The input string is guaranteed to have characters and frequencies alternating, but the frequencies may have more than one digit.
"""

def find_longest_run(s):
    s = list(map(str, s))
    numbers = [int(s[i]) for i in range(1,len(s),2)]
    chars = [s[i] for i in range(0,len(s),2)]
    pairs = list(zip(chars,numbers))
    longest_run_char = max(pairs, key=lambda pair:pair[1])
    return longest_run_char[0]