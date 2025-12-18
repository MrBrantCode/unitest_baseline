"""
QUESTION:
Write a function named `custom_histogram` that takes a string `test` as input and returns a dictionary containing the count of each unique character (both upper and lower case letters, and punctuation marks) in the string. The keys in the dictionary should be in lower-case format and include the count of each character, separated by an underscore. If multiple characters have the same frequency, include them all in the output. The function should handle empty strings and return an empty dictionary in such cases.
"""

def custom_histogram(test):
    import string
    freq = {}

    # looping over every character in the string
    for char in test:
        # checking if the character is a letter or punctuation
        if char.isalpha() or char in string.punctuation:
            lower_char = char.lower()
            if lower_char not in freq:
                freq[lower_char] = 1
            else:
                freq[lower_char] += 1

    output_freq = {}

    # Formatting output dictionary keys with counts
    for key, value in freq.items():
        output_freq[key + '_' + str(value)] = value

    return output_freq