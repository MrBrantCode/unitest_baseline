"""
QUESTION:
Write a function `most_least_frequent_strings` that takes a list of strings as input and returns an object with two keys, "most_frequent" and "least_frequent", containing lists of the most and least frequent strings respectively. 

The function should check if the input list is empty, and if so, return an empty list. It should also check if all elements in the list are strings, and if not, return an error message.

The function should consider accented characters and different case variants as the same string for comparison purposes. If there are ties for most or least frequent strings, the corresponding list should contain all the tied strings. If there are no least frequent strings (i.e., all strings in the input list occur with the same frequency), the "least_frequent" list should be empty.

The input list can contain strings in any language.
"""

import unicodedata

def most_least_frequent_strings(strings):
    # Check if input array is empty
    if not strings:
        return []

    # Check if input array contains only strings
    if not all(isinstance(s, str) for s in strings):
        return "Error: Input array should contain only strings"

    # Remove accents from strings and convert to lowercase
    normalized_strings = [unicodedata.normalize("NFKD", s).encode("ASCII", "ignore").decode().lower() for s in strings]

    # Count frequency of each string
    frequency = {}
    for s in normalized_strings:
        if s in frequency:
            frequency[s] += 1
        else:
            frequency[s] = 1

    # Find most and least frequent strings
    max_frequency = max(frequency.values())
    min_frequency = min(frequency.values())
    most_frequent = [s for s, count in frequency.items() if count == max_frequency]
    least_frequent = [s for s, count in frequency.items() if count == min_frequency and count != max_frequency]

    # Return result as an object
    return {"most_frequent": most_frequent, "least_frequent": least_frequent}