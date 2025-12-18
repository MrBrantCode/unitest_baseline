"""
QUESTION:
Develop a function named `shared_chars_count` that takes two string parameters, `str1` and `str2`. The function should return a dictionary where the keys are the shared characters between `str1` and `str2` (ignoring case) and the values are the minimum number of occurrences of each shared character in both strings. The function should also handle special characters and numbers.
"""

def shared_chars_count(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    common_chars = set(str1) & set(str2)

    freq_count = {}

    for char in common_chars:
        freq_count[char] = min(str1.count(char), str2.count(char))

    return freq_count