"""
QUESTION:
Create a function called `normalize_dataset` that takes a list of strings representing locations in the format "City, State/Province" and returns a list of normalized strings with no leading or trailing spaces and proper capitalization, along with a dictionary containing each unique normalized string and its occurrence count. The function should handle variations in capitalization, leading/trailing spaces, and abbreviations for states/provinces, and exclude duplicate normalized strings from the output dictionary.
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