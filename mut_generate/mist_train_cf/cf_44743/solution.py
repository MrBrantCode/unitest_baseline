"""
QUESTION:
Develop a function called `check_anagram` that takes a list of strings as input and returns a boolean value indicating whether all the strings in the list are anagrams of each other. The function should assume that the input list contains at least two words.
"""

def check_anagram(a_list):
    # Assuming the list consists of at least 2 words
    chars_in_first_word = sorted(a_list[0])

    # Check the rest of the list
    for word in a_list[1:]:
        chars_in_word = sorted(word)

        if chars_in_first_word != chars_in_word:
            return False

    return True