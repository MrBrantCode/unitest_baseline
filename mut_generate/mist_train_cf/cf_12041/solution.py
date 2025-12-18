"""
QUESTION:
Write a function `count_occurrences` that takes a string and a character as arguments. The function should count the number of occurrences of the character in the string, excluding occurrences where the character is preceded or followed by another instance of the same character. The function should be case-sensitive.
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