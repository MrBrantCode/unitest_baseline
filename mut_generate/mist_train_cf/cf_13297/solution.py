"""
QUESTION:
Create a function named `remove_duplicates` that takes an array of elements as input and returns a list of unique elements in descending order based on their frequency. The function should also keep track of the count of each unique element.
"""

from collections import Counter

def remove_duplicates(array):
    counter = Counter(array)  # Count the occurrences of each element
    unique_elements = list(counter.keys())  # Get the unique elements
    unique_elements.sort(key=lambda x: counter[x], reverse=True)  # Sort the unique elements by their count in descending order
    return unique_elements