"""
QUESTION:
Write a function `min_frequency_name` that takes a dictionary where keys are names and values are their frequencies. Return the name with the minimum frequency. If multiple names have the same minimum frequency, return the name that is alphabetically first.
"""

def min_frequency_name(dic):
    min_frequency = min(dic.values())
    min_frequency_names = [name for name, frequency in dic.items() if frequency == min_frequency]
    return min(sorted(min_frequency_names))