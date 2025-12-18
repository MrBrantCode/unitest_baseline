"""
QUESTION:
Write a function `distinct_echo_substrings` that takes a string `text` as input and returns the number of distinct non-empty substrings that can be written as the concatenation of some string with itself (`a + a`) and are also palindromes. The input `text` is guaranteed to have a length between 1 and 2000 and only contains lowercase English letters.
"""

def distinct_echo_substrings(text):
    substrings = set()
    for length in range(1, len(text) // 2 + 1):
        for i in range(len(text) - length * 2 + 1):
            substring = text[i:i + length]
            if substring == substring[::-1] and text[i:i + length * 2] == substring + substring:
                substrings.add(substring + substring)
    return len(substrings)