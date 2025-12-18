"""
QUESTION:
Implement a function `popular_tags` that takes a list of strings representing tags as input, and returns a list of the top 5 most popular tags in descending order of their frequency. If there are fewer than 5 unique tags, return all unique tags. The function should be case-sensitive and return tags in their original case.
"""

from collections import Counter
from typing import List

def popular_tags(tags: List[str]) -> List[str]:
    tag_counts = Counter(tags)
    sorted_tags = sorted(tag_counts, key=lambda x: (-tag_counts[x], x))
    return sorted_tags[:5]