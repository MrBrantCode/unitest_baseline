"""
QUESTION:
Write a function `group_and_sort_words` that takes a list of words as input and returns a sorted list of tuples, where each tuple contains a group letter, the frequency count of the group, and the list of words in the group. The groups are formed by the first letter of each word. The output should be sorted first by group frequency in descending order and then by the last character of the group letter in ascending order.
"""

from collections import defaultdict

def group_and_sort_words(words):
    """
    This function takes a list of words as input, groups them by their first letter, 
    and returns a sorted list of tuples. Each tuple contains the group letter, 
    the frequency count of the group, and the list of words in the group. 
    The output is sorted first by group frequency in descending order and then 
    by the last character of the group letter in ascending order.
    
    Args:
    words (list): A list of words.
    
    Returns:
    list: A sorted list of tuples containing the group letter, frequency count, 
          and the list of words in the group.
    """
    
    # Group the words by their first letter
    groups = defaultdict(list)
    for word in words:
        groups[word[0]].append(word)
    
    # Count the number of words in each group
    group_freq = {}
    for group, words in groups.items():
        group_freq[group] = len(words)
    
    # Sort the groups by frequency and last character of the group letter
    sorted_groups = sorted(groups.items(), key=lambda x: (-group_freq[x[0]], x[0][-1]))
    
    # Return a list of tuples containing the group letter, frequency count, and words
    return [(group, group_freq[group], words) for group, words in sorted_groups]