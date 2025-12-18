"""
QUESTION:
Write a function `min_frequency_names` that takes a dictionary of names and their frequencies as input. The function should return a list of names with the minimum frequency, sorted in descending alphabetical order. If multiple names have the same minimum frequency, all of them should be included in the output list. If the input dictionary is empty, the function should return an empty list.
"""

def min_frequency_names(frequencies):
    if not frequencies:
        return []

    min_frequency = min(frequencies.values())
    min_frequency_names = [name for name, frequency in frequencies.items() if frequency == min_frequency]

    return sorted(min_frequency_names, reverse=True)