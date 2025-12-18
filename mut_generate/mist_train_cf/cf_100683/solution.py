"""
QUESTION:
Create a function `most_least_frequent_strings(strings)` that takes an array of strings as input and returns an object containing the most and least frequent strings. The function should check if the input array is empty or contains non-string values, and handle accented characters and different case variants as the same string.
"""

import unicodedata

def most_least_frequent_strings(strings):
    if not strings:
        return []

    if not all(isinstance(s, str) for s in strings):
        return "Error: Input array should contain only strings"

    normalized_strings = [unicodedata.normalize("NFKD", s).encode("ASCII", "ignore").decode().lower() for s in strings]

    frequency = {}
    for s in normalized_strings:
        if s in frequency:
            frequency[s] += 1
        else:
            frequency[s] = 1

    max_frequency = max(frequency.values())
    min_frequency = min(frequency.values())
    most_frequent = [s for s, count in frequency.items() if count == max_frequency]
    least_frequent = [s for s, count in frequency.items() if count == min_frequency]

    return {"most_frequent": most_frequent, "least_frequent": least_frequent}