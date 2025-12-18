"""
QUESTION:
Develop a function named `cap_first_letters` that takes a string as an argument and returns a string where the first letter of each word is in uppercase. The function should ignore numbers and special characters, and treat multiple consecutive whitespace characters as a single space.
"""

def cap_first_letters(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if words[i].isalpha():
            words[i] = words[i][0].upper() + words[i][1:]
    return ' '.join(words)