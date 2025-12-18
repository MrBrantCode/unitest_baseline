"""
QUESTION:
Create a function `analyze_string` that takes an input string and returns a sorted list of tuples. Each tuple should contain an alphabetical character (ignoring case differences) and its frequency in the string, in descending order of frequency. Non-alphabetical characters should be ignored in the frequency analysis.
"""

def analyze_string(input_string):
    freq_dict = {}
    for char in input_string:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in freq_dict:
                freq_dict[char_lower] += 1
            else:
                freq_dict[char_lower] = 1

    sorted_list = sorted(freq_dict.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_list