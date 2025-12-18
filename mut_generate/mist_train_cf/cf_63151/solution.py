"""
QUESTION:
Implement a function named `replace_strings` that takes a target string and two lists of strings as input. The function should replace all whole instances of the strings in the first list with their corresponding strings in the second list within the target string, ignoring instances where the strings appear as substrings within other words. If the lists are of unequal lengths, unmatched strings in the first list should be left unchanged and unmatched strings in the second list should be ignored. The function should be efficient enough to process large amounts of data.
"""

def replace_strings(target, list1, list2):
    replacement_dict = dict(zip(list1, list2))
    
    words = target.split()
    for i, word in enumerate(words):
        if word in replacement_dict:
            words[i] = replacement_dict[word]
    
    return ' '.join(words)