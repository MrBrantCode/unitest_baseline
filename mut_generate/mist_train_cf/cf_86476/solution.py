"""
QUESTION:
Find the length of the longest substring of a string that contains only vowels, starts and ends with a consonant, and has at least one digit in it. Return the starting and ending indices of this longest substring as well. The function should be named `longest_substring(text)` and it takes one parameter, the input string `text`.
"""

def longest_substring(text):
    vowels = set('aeiouAEIOU')
    start = -1
    end = -1
    maxLength = 0

    for i in range(len(text)):
        if text[i] not in vowels and not text[i].isdigit():  # Consonant
            if i > 0 and text[i-1] in vowels:  # Check if previous character is a vowel
                start = i-1
        else:  # Vowel or digit
            if i < len(text)-1 and text[i+1] not in vowels and not text[i+1].isdigit():  # Check if next character is a consonant
                end = i+1
            if text[i].isdigit() and start != -1 and end != -1 and end - start + 1 > maxLength:  # Check if current substring meets conditions
                maxLength = end - start + 1

    return maxLength, start, end