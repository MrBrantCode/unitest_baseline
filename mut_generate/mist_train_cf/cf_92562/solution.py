"""
QUESTION:
Write a function named `normalize_dataset` that takes a list of strings representing locations in the format "City, State/Province" and returns a list of normalized strings and a dictionary containing the occurrences of each unique normalized string. The normalization process should handle variations in capitalization, leading/trailing spaces, and abbreviations for states/provinces, and the occurrences dictionary should not include duplicate normalized strings.
"""

def normalize_dataset(dataset):
    normalized_dataset = []
    occurrences = {}
    
    for string in dataset:
        normalized_string = string.strip().title()
        
        if normalized_string in occurrences:
            occurrences[normalized_string] += 1
        else:
            occurrences[normalized_string] = 1
        
        normalized_dataset.append(normalized_string)
    
    return normalized_dataset, occurrences