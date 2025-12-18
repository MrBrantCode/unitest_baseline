"""
QUESTION:
Write a function named `reverse_join_vowels` that takes a list of strings as input. The function should join the strings that start with a vowel (A, E, I, O, U) with a pipe (|) and return the resulting string reversed. The function must achieve this with a time complexity of O(n) and a space complexity of O(n) is not achievable in this case since we need to store the resulting string, but it should be as efficient as possible.
"""

def reverse_join_vowels(words):
    vowels = set(['A', 'E', 'I', 'O', 'U'])
    result = ""
    for word in words:
        if word[0].upper() in vowels:
            result += word + "|"
    return result[:-1][::-1]