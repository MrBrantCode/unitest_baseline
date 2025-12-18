"""
QUESTION:
Write a function named `replace_sequence` that takes four parameters: a context string `string`, a target character sequence `string1`, a replacement character sequence `string2`, and an integer `n`. The function should replace the `n`th and subsequent occurrences of `string1` in `string` with `string2` and return the modified string.
"""

def replace_sequence(string, string1, string2, n):
    count = 0
    words = string.split()
    for i, word in enumerate(words):
        if word == string1:
            count += 1
            if count >= n:
                words[i] = string2
    return ' '.join(words)