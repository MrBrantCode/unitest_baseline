"""
QUESTION:
Write a function named `count_occurrences` that takes two arguments: `string` and `char`. The function should count the number of occurrences of `char` in `string`, where `char` is not preceded or followed by the same character. The function should be case-sensitive, and the string can contain both uppercase and lowercase letters, special characters, and numbers.
"""

def count_occurrences(string, char):
    count = 0
    for i in range(len(string)):
        if string[i] == char:
            # Check if the character is not preceded or followed by the same character
            if i == 0 or string[i-1] != char:
                if i == len(string) - 1 or string[i+1] != char:
                    count += 1
    return count