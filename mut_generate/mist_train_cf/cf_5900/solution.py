"""
QUESTION:
Create a function called `normalize_dataset` that takes a dataset of strings representing locations in the format "City, State/Province" and returns a list of normalized strings and a dictionary containing the occurrences of each unique normalized string.

The function should normalize the strings by removing leading/trailing spaces and capitalizing the first letter of each word. It should then count the occurrences of each unique normalized string and store them in a dictionary. The function should handle duplicate strings in the dataset and exclude them from the output list, but include their occurrences in the dictionary.
"""

def normalize_dataset(dataset):
    occurrences_dict = {}
    normalized_dataset = []

    for location in dataset:
        normalized_location = location.strip().title()

        if normalized_location not in normalized_dataset:
            normalized_dataset.append(normalized_location)

        if normalized_location in occurrences_dict:
            occurrences_dict[normalized_location] += 1
        else:
            occurrences_dict[normalized_location] = 1

    return normalized_dataset, occurrences_dict