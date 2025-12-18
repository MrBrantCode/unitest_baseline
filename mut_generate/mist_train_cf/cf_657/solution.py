"""
QUESTION:
Write a function named `remove_substring` that takes two parameters: `string` and `substring`. The function should remove all occurrences of `substring` from `string` if `substring` is a standalone word and not part of a larger word, while maintaining the original order of the characters in `string`. The function is case-sensitive and should not remove `substring` if it is part of a larger word.
"""

def remove_substring(string, substring):
    words = string.split()
    result = []
    for word in words:
        if word != substring:
            result.append(word)
        else:
            result.append('')
    return ' '.join(result)