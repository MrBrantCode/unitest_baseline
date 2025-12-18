"""
QUESTION:
Implement a function `is_sad_complex(s)` that takes a string `s` as input. The string `s` is considered 'sad' if it consists of more than three characters and each group of three consecutive letters is identical. Additionally, each unique letter appears only once or repeats consecutively. The function must use a dictionary to store character occurrences throughout the analysis process.
"""

def is_sad_complex(s):
    dictionary = dict()

    for i in range(len(s)):
        if s[i] in dictionary:
            if i > 1 and s[i - 1] == s[i - 2] == s[i]:
                return False
            dictionary[s[i]] += 1
        else:
            dictionary[s[i]] = 1

    for key, value in dictionary.items():
        if value > 2:
            return False

    return len(s) > 3 and all(s[i:i+3] == s[i+1:i+4] for i in range(len(s) - 3))