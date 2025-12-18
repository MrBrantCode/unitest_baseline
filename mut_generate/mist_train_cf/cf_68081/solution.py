"""
QUESTION:
Implement a function `find_substrings(s)` that takes a string `s` as input and returns all longest substrings with no repeating characters along with their corresponding starting and ending indices. The function should not use any built-in functions for obtaining substrings. If there are multiple longest substrings with no repeating characters, return all possible substrings. The function should handle edge cases such as when the length of the string is 0 or 1, or when the string has all repeated or all distinct characters.
"""

def find_substrings(s):
    # Check if the string is empty or has only one character
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [(s[0], 0, 0)]

    seen = {}
    answer = [] 
    max_length = 0
    start = 0

    for i, letter in enumerate(s):
        if letter in seen and start <= seen[letter]:
            start = seen[letter] + 1
        else:
            if (i - start + 1) > max_length:
                max_length = i - start + 1 
                answer = [(s[start:i+1], start, i)]
            elif (i - start + 1) == max_length:
                answer.append((s[start:i+1], start, i))

        seen[letter] = i

    return answer