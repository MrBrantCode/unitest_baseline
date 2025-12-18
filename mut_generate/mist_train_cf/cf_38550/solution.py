"""
QUESTION:
Implement a function named `organize_entries` that takes a list of dictionaries as input. Each dictionary in the list represents an entry with keys 'word', 'tag', and 'synonyms'. The function should return a dictionary where the keys are the part of speech tags and the values are lists of words corresponding to each tag. The function should also replace underscores with spaces in the synonyms.
"""

def organize_entries(entries: list) -> dict:
    organized_dict = {}
    for entry in entries:
        tag = entry['tag']
        word = entry['word']
        synonyms = [syn.replace('_', ' ') for syn in entry['synonyms']]
        if tag in organized_dict:
            organized_dict[tag].append(word)
        else:
            organized_dict[tag] = [word]
        entry['synonyms'] = synonyms
    return organized_dict