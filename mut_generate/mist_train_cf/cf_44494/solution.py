"""
QUESTION:
Implement a function named `find_word_indices` that takes in a list of strings `word_list` and a search term `term`, and returns a list of indices where the term occurs in the list. If the term is not found, return -1. The function should perform a case-insensitive search and handle edge cases where the term occurs within other words. The function should be efficient enough to handle large lists.
"""

def find_word_indices(word_list, term):
  indices = [i for i, x in enumerate(word_list) if x.lower() == term.lower()]
  return indices if indices else -1