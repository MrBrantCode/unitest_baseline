"""
QUESTION:
Write a function `evaluate_and_correct_paragraph` that accepts a paragraph and two parameters: a dictionary `uncommon_punctuation_map` where keys are uncommon punctuation marks and values are their common equivalents, and a string `common_punctuation` of common punctuation marks. The function should return a dictionary where keys are uncommon punctuation marks and ascii characters found in the paragraph and their frequencies are the corresponding values, and the paragraph with uncommon punctuation marks replaced by their common equivalents.
"""

import string
from collections import Counter

def evaluate_and_correct_paragraph(paragraph, uncommon_punctuation_map, common_punctuation):
    uncommon_characters = set(uncommon_punctuation_map.keys()) | set(common_punctuation)
    frequency_dict = Counter(paragraph)

    uncommon_characters_dict = {ch: frequency_dict[ch] for ch in uncommon_characters if ch in frequency_dict}

    for uncommon, common in uncommon_punctuation_map.items():
        paragraph = paragraph.replace(uncommon, common)

    return uncommon_characters_dict, paragraph