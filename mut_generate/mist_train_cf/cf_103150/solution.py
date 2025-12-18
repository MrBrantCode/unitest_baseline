"""
QUESTION:
Create a function called `calculate_frequency` that takes a list as input and returns a list of tuples containing each unique element and its frequency in descending order of frequency.
"""

def calculate_frequency(lst):
    frequency = {}
    for element in lst:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return sorted(frequency.items(), key=lambda x: x[1], reverse=True)