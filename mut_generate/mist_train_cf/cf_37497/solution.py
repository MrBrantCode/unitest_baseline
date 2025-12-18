"""
QUESTION:
Write a function `analyze_tags(tags: List[str]) -> Dict[str, int]` that takes a list of tags as input where each tag is a string with a specific format separated by '::'. The function should categorize the tags into different groups based on the common prefixes before the double colons (::) and return a dictionary where the keys are the distinct tag groups and the values are the counts of occurrences for each group.
"""

from typing import List, Dict

def analyze_tags(tags: List[str]) -> Dict[str, int]:
    tag_counts = {}
    for tag in tags:
        group = tag.split('::')[0].strip()
        tag_counts[group] = tag_counts.get(group, 0) + 1
    return tag_counts