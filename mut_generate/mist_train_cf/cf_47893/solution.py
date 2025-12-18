"""
QUESTION:
Write a function called `anagram_checker` that takes a list of strings as input and returns `True` if all strings are anagrams of each other and `False` otherwise. The function should ignore case and any leading, trailing or intermediate white spaces. The function should not handle punctuation, special characters, or strings in different languages. The input list must contain at least two strings.
"""

def anagram_checker(strings):
    
    # check if number of strings is less than 2
    if len(strings) < 2:
        return False

    # convert all strings to lowercase and remove white spaces
    strings = [s.replace(" ", "").lower() for s in strings]

    # sort the characters in the strings and compare them
    sorted_strings = [''.join(sorted(s)) for s in strings]

    # if all sorted strings are equal, the strings are anagrams
    return len(set(sorted_strings)) == 1