"""
QUESTION:
Write a function named `most_frequent_char` that takes a string as input, returns the most frequently used alphabetical character in the string (case-insensitive), and ignores any duplicate characters that occur consecutively. The function should handle strings that contain non-alphabetical characters and achieve a time complexity of O(n), where n is the length of the string.
"""

def most_frequent_char(string):
    freq = {}  # dictionary to store the frequency of each character
    max_freq = 0  # variable to track the maximum frequency
    most_freq_char = ''  # variable to store the most frequently used character
    prev_char = None  # variable to track the previous character

    # convert the string to lowercase
    string = string.lower()

    # iterate over the characters in the string
    for char in string:
        # check if the character is alphabetical
        if char.isalpha():
            # check if the character is not a consecutive duplicate
            if char != prev_char:
                # check if the character is already in the dictionary
                if char in freq:
                    freq[char] += 1
                else:
                    # if the character is not in the dictionary, add it with frequency 1
                    freq[char] = 1

            # update the previous character
            prev_char = char

            # update the maximum frequency and most frequently used character if necessary
            if freq[char] > max_freq:
                max_freq = freq[char]
                most_freq_char = char

    return most_freq_char