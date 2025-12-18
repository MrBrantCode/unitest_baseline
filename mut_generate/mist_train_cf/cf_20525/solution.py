"""
QUESTION:
Write a function `normalize_dataset` that takes a list of strings representing locations in the format "City, State/Province" and returns two values:
- A list of normalized strings, where each string has no leading or trailing spaces and the city and state/province names are capitalized properly.
- A dictionary where each unique normalized string is a key and the number of occurrences of that normalized string is the value.

The function should handle variations in capitalization and leading/trailing spaces. The order of the strings in the normalized dataset and the occurrences dictionary does not matter. Assume the input list will only contain valid location strings and will not be empty.
"""

def normalize_dataset(dataset):
    normalized_dataset = []
    occurrences_dict = {}
    for string in dataset:
        normalized_string = string.strip().title()
        if normalized_string in occurrences_dict:
            occurrences_dict[normalized_string] += 1
        else:
            occurrences_dict[normalized_string] = 1
        normalized_dataset.append(normalized_string)
    return normalized_dataset, occurrences_dict