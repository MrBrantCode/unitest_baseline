"""
QUESTION:
Write a function named check_anagram that takes two strings, first and second, as input and returns True if they are anagrams and False otherwise. The function should consider all characters in the strings and be case insensitive. The time complexity of the function should be O(n), where n is the length of the longest string.
"""

def check_anagram(first, second):
    # Removing all non-alphanumeric characters from both strings and converting to lowercase
    first = ''.join(e for e in first if e.isalnum()).lower()
    second = ''.join(e for e in second if e.isalnum()).lower()

    # If the lengths of the strings are different, they cannot be anagrams
    if len(first) != len(second):
        return False

    # Counting the frequency of each character in the first string
    char_count = {}
    for char in first:
        char_count[char] = char_count.get(char, 0) + 1

    # Decrementing the frequency of each character in the second string
    # If any character is not present or its frequency becomes negative, they cannot be anagrams
    for char in second:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
        else:
            return False

    # If all characters have been cancelled out, they are anagrams
    if len(char_count) == 0:
        return True
    else:
        return False