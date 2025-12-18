"""
QUESTION:
Write a function `find_longest_vowel_word` that finds the longest word in a given string that starts with a vowel, handling both uppercase and lowercase vowels. The function should return `None` if no word starting with a vowel is present. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1), excluding the space required for the input and output.
"""

def find_longest_vowel_word(string):
    vowels = "aeiou"
    longest_word = None
    current_word = ""
    for char in string:
        if char.isalpha():
            current_word += char.lower()
        elif current_word and current_word[0] in vowels:
            if longest_word is None or len(current_word) > len(longest_word):
                longest_word = current_word
            current_word = ""
        else:
            current_word = ""
    if current_word and current_word[0] in vowels:
        if longest_word is None or len(current_word) > len(longest_word):
            longest_word = current_word
    return longest_word