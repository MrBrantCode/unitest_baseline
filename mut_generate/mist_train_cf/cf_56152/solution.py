"""
QUESTION:
Given a list of strings, write a function named `reverse_pairs` that returns the number of pairs of inverse strings present within the list. A pair of inverse strings is defined as two strings that are reverse of each other. The function should have a time complexity of O(n*m*log(m)) and a space complexity of O(n), where n is the number of unique strings in the list and m is the average length of the strings.
"""

def reverse_pairs(lst):
    from collections import defaultdict

    # Create a dictionary to store the canonical form frequency
    canon_freq = defaultdict(int)
    
    # Populate the canonical form frequency
    for string in lst:
        string_rev = string[::-1]
        canon = min(string, string_rev)
        canon_freq[canon] += 1

    # Count the total number of pairs
    pairs = 0
    for freq in canon_freq.values():
        pairs += freq * (freq - 1) // 2

    return pairs