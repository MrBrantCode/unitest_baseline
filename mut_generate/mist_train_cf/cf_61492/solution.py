"""
QUESTION:
Create a function named `char_freq_and_first_unique` that takes a list of strings as input. The function should return a dictionary where each key is a string from the input list and its corresponding value is another dictionary containing two key-value pairs: 'first_unique_char_index' and 'frequency_dist'. The 'first_unique_char_index' should store the index of the first unique character in the string, or -1 if no unique character exists. The 'frequency_dist' should store a list of tuples, each containing a character from the string and its frequency, sorted in increasing order by character. All characters should be treated as lowercase for the purpose of frequency distribution count.
"""

def char_freq_and_first_unique(str_list):
    result = dict()
    for s in str_list:
        char_freq = dict()
        for c in s:
            c = c.lower()
            if c in char_freq:
                char_freq[c] += 1
            else:
                char_freq[c] = 1

        first_unique_char_index = -1           # Set initial index as -1
        for i, c in enumerate(s):
            c = c.lower()
            if char_freq[c] == 1:               # Employ frequency dict to find first unique char
                first_unique_char_index = i     # Update index if first unique char is found
                break

        sorted_char_freq = sorted(char_freq.items(), key=lambda x: x[0])    # sort char frequency dist
        result[s] = {
            'first_unique_char_index': first_unique_char_index,
            'frequency_dist': sorted_char_freq
        }
    return result