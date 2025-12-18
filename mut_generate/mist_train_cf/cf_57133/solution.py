"""
QUESTION:
Create a function called `are_anagrams` that takes two string parameters `string_1` and `string_2`. The function should determine if the two input strings are anagrams of each other by checking if they contain the same characters with the same frequency, disregarding spaces and case.
"""

def are_anagrams(string_1, string_2):
    # Remove spaces and convert to lower case
    string_1 = string_1.replace(" ", "").lower()
    string_2 = string_2.replace(" ", "").lower()

    # If the two strings have different lengths, they are not anagrams
    if len(string_1) != len(string_2):
        return False

    # Create a dictionary to store the frequency of each character in the first string
    char_count = {}

    for char in string_1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Subtract the frequency of each character in the second string
    # If we end up with a zero for each character, the strings are anagrams
    # If any character count is not zero, the strings are not anagrams
    for char in string_2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False

    return all(value == 0 for value in char_count.values())