"""
QUESTION:
Design a function named `exclusive_entries` that takes two unordered lists of string values as input, identifies the exclusive entries (i.e., the entries that appear in only one of the lists), and returns these entries along with their total count.
"""

def exclusive_entries(list1, list2):
    combined = list1 + list2
    counts = {}
    for entry in combined:
        if entry in counts:
            counts[entry] += 1
        else:
            counts[entry] = 1
    exclusives = [entry for entry, count in counts.items() if count == 1]
    return exclusives, len(exclusives)