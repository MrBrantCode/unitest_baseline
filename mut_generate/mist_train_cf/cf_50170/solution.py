"""
QUESTION:
Construct a function named `count_reverse_pairs` that takes a list of strings as input and returns the number of unique reversed string pairs. The function should ignore special characters, numerals, case sensitivity, spaces, and unicode characters when counting the reversed string pairs. Duplicate strings should be considered as the same string when counting the pairs.
"""

def count_reverse_pairs(lst):
    count = 0
    seen_pairs = set()
    cleaned_lst = [''.join(filter(str.isalpha, s)).lower() for s in lst]
    for i in range(len(cleaned_lst)):
        for j in range(i+1, len(cleaned_lst)):
            pair = tuple(sorted([cleaned_lst[i], cleaned_lst[j]]))
            if cleaned_lst[i] == cleaned_lst[j][::-1] and pair not in seen_pairs:
                count += 1
                seen_pairs.add(pair)
    return count