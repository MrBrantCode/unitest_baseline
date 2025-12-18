"""
QUESTION:
Implement the function `process_metadata(metadata_list: List[str]) -> Tuple[Dict[str, int], Dict[str, int]]` to process a list of strings representing metadata for Python packages. Each string contains information about the programming language compatibility and the topic of the package in the format 'Category :: Value'. The function should return a tuple containing two dictionaries: one with the count of each unique programming language compatibility and the other with the count of each unique topic covered by the packages. Assume that the input list only contains metadata in the required format, with categories 'Programming Language' and 'Topic'.
"""

from typing import List, Dict, Tuple

def process_metadata(metadata_list: List[str]) -> Tuple[Dict[str, int], Dict[str, int]]:
    programming_language_counts = {}
    topic_counts = {}

    for metadata in metadata_list:
        category, value = metadata.split(' :: ')
        if category.startswith('Programming Language'):
            programming_language_counts[value] = programming_language_counts.get(value, 0) + 1
        elif category.startswith('Topic'):
            topic_counts[value] = topic_counts.get(value, 0) + 1

    return programming_language_counts, topic_counts