"""
QUESTION:
Create a function `parse_metadata(metadata_list)` that takes a list of strings as input where each string contains metadata in the form of key-value pairs separated by double colons (::). Return a dictionary containing the parsed metadata, where the keys are the attributes (e.g., "License", "Programming Language") and the values are lists of the specific details for each attribute.
"""

def parse_metadata(metadata_list):
    metadata_dict = {}
    for metadata in metadata_list:
        key, value = metadata.split(' :: ')
        if key in metadata_dict:
            metadata_dict[key].append(value)
        else:
            metadata_dict[key] = [value]
    return metadata_dict