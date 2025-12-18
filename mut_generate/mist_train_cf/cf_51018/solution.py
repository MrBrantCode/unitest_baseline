"""
QUESTION:
Design a function named `process_string` that takes a string `s` as input, and returns a dictionary with two keys: `first_unique_char_index` and `frequency_dist`. The function should consider all characters as lowercase, and ignore any irrelevant information.

The function should determine the index of the first character in the string that appears only once (`first_unique_char_index`), and the frequency distribution of each alphabet in the string (`frequency_dist`), which is a list of tuples containing each unique alphabet and its frequency, sorted in ascending order by alphabet.

The function should return a dictionary with the following structure:
- `first_unique_char_index`: the index of the first unique character in the string
- `frequency_dist`: a list of tuples, where each tuple contains an alphabet and its frequency in the string, sorted in ascending order by alphabet.
"""

def process_string(s):
    # change all characters to lowercase
    s = s.lower()

    # count the frequency of each character in the string
    freq_count = {}
    for char in s:
        if char in freq_count:
            freq_count[char] += 1
        else:
            freq_count[char] = 1

    # find the first unique character in the string
    first_unique_char_index = next((index for index, char in enumerate(s) if freq_count[char] == 1), None)

    # sort the frequency distribution
    frequency_dist = sorted(freq_count.items())

    return {
        'first_unique_char_index': first_unique_char_index,
        'frequency_dist': frequency_dist
    }