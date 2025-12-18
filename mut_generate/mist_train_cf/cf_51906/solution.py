"""
QUESTION:
Write a function `replace_phrases(s)` that uses regular expressions to identify and replace a specific phrase in a given string `s`. The function should replace "an apple a day keeps the doctor away" with "a healthy lifestyle keeps diseases at bay" in a case-insensitive manner, handling edge cases such as punctuation and the presence of the phrase within a larger context. The function should return the modified string and the number of successful replacements made.
"""

import re

def replace_phrases(s):
    pattern = re.compile(r'(?i)an apple a day keeps the doctor away') 
    count = 0
    lines = s.split('\n')
    for i in range(len(lines)):
        if re.search(pattern, lines[i]):
            lines[i] = re.sub(pattern, 'a healthy lifestyle keeps diseases at bay', lines[i])
            count += 1
    return '\n'.join(lines), count