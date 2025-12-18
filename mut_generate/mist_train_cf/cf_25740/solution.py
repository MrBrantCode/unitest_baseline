"""
QUESTION:
Write a function named `most_frequent_letter` that takes a string `s` as input and returns the letter that appears most frequently in the string. The function should ignore non-letter characters and consider the frequency of each letter regardless of its case (e.g., 'A' and 'a' are considered the same letter). If there are multiple letters with the same highest frequency, return any one of them.
"""

def most_frequent_letter(s):
    # convert the string to lower case and filter non-letter characters
    s = ''.join(filter(str.isalpha, s)).lower()
    
    # get the letter frequency
    letter_frequency = {}
    for ch in s:
        if ch in letter_frequency:
            letter_frequency[ch] += 1
        else:
            letter_frequency[ch] = 1

    # find the letter with the max frequency
    max_frequency = 0
    max_frequency_letter = ''
    for letter, frequency in letter_frequency.items():
        if frequency > max_frequency:
            max_frequency = frequency
            max_frequency_letter = letter

    return max_frequency_letter