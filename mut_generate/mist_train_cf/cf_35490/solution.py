"""
QUESTION:
Write a function `parse_metadata(metadata_list)` that takes a list of strings as input where each string is in the format 'Category :: Value' and returns a dictionary containing the parsed metadata. The function should group the values by category and store them in lists. Categories include 'Operating System', 'Programming Language', and 'Topic'. The function should handle duplicate values.
"""

def parse_metadata(metadata_list):
    parsed_metadata = {
        'Operating System': [],
        'Programming Language': [],
        'Topic': []
    }

    for metadata in metadata_list:
        category, value = metadata.split('::')
        category = category.strip()
        value = value.strip()
        if category in parsed_metadata:
            parsed_metadata[category].append(value)

    return parsed_metadata