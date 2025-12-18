"""
QUESTION:
Write a function `replace_substring(sentence, substring, replacement)` that replaces all occurrences of a given `substring` in a `sentence` while ignoring case sensitivity. The function should remove any leading or trailing whitespaces in the `sentence` before performing the replacement. The function should output the modified sentence. The function should have a time complexity of O(n), where n is the length of the sentence. Do not use any built-in functions or methods that directly perform the replacement or case-insensitive search.
"""

def replace_substring(sentence, substring, replacement):
    sentence = sentence.strip()
    modified_sentence = []
    lowercase_substring = substring.lower()
    lowercase_sentence = sentence.lower()

    i = 0
    while i < len(lowercase_sentence):
        if lowercase_sentence[i:i+len(lowercase_substring)] == lowercase_substring:
            modified_sentence.extend(replacement)
            i += len(lowercase_substring)
        else:
            modified_sentence.append(sentence[i])
            i += 1

    return ''.join(modified_sentence)