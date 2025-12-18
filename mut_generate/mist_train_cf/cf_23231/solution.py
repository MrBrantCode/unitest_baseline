"""
QUESTION:
Replace all non-overlapping occurrences of multiple substrings with a replacement substring in a given string while maintaining the original order of characters. The function `replace_substring` should take three parameters: the original string, a list of substrings to be replaced, and the replacement substring.
"""

def replace_substring(string, substrings, replacement):
    modified_substrings = []
    i = 0

    while i < len(string):
        found = False
        for substring in substrings:
            if string[i:].startswith(substring):
                modified_substrings.append(replacement)
                i += len(substring)
                found = True
                break
        if not found:
            modified_substrings.append(string[i])
            i += 1

    return ''.join(modified_substrings)