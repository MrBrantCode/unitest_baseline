"""
QUESTION:
Implement a function `special_sort(words, special_chars)` that takes in a list of strings `words` and a list of characters `special_chars`, and returns the sorted list of `words`. The sorting rule is as follows: if a word contains any character from `special_chars`, it should be sorted in ascending lexicographic order; otherwise, it should be sorted in reverse lexicographic order.
"""

def special_sort(words, special_chars):
    def compare(word):
        return (all(c not in word for c in special_chars), word)
    return sorted(words, key=compare, reverse=True)