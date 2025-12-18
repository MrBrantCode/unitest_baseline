"""
QUESTION:
Write a function `replace_substring(sentence, substring, replacement)` that replaces all occurrences of a given `substring` in a `sentence` with `replacement` while ignoring case sensitivity. The function should remove any leading or trailing whitespaces in the `sentence` before performing the replacement. It should have a time complexity of O(n), where n is the length of the `sentence`. The function cannot use any built-in functions or methods that directly perform the replacement or case-insensitive search.
"""

def replace_substring(sentence, substring, replacement):
    # Remove leading and trailing whitespaces
    sentence = sentence.strip()

    # Create an empty list to store the modified sentence
    modified_sentence = []

    # Convert the substring and sentence to lowercase for case-insensitive comparison
    lowercase_substring = substring.lower()
    lowercase_sentence = sentence.lower()

    # Iterate over the sentence and find the occurrences of the lowercase substring
    i = 0
    while i < len(lowercase_sentence):
        # Check if the lowercase substring is found at the current position
        if lowercase_sentence[i:i+len(lowercase_substring)] == lowercase_substring:
            # If found, append the replacement to the modified sentence
            modified_sentence.extend(replacement)
            # Move the index to the end of the substring
            i += len(lowercase_substring)
        else:
            # If not found, append the current character to the modified sentence
            modified_sentence.append(sentence[i])
            i += 1

    # Join the characters in the modified sentence list and return the final result
    return ''.join(modified_sentence)