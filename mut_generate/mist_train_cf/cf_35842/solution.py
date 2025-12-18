"""
QUESTION:
Write a function `process_metadata` that takes a list of strings `metadata` as input, where each string represents a line of metadata in the format "key: value". The function should return a dictionary containing the extracted information, where keys are the metadata keys and values are the corresponding metadata values. If a key appears multiple times in the metadata, the function should concatenate the values into a single string, separating them with commas.
"""

def process_metadata(metadata):
    extracted_info = {}
    for line in metadata:
        key, value = line.split(':')
        key = key.strip()
        value = value.strip()
        if key in extracted_info:
            extracted_info[key] += f", {value}"
        else:
            extracted_info[key] = value
    return extracted_info