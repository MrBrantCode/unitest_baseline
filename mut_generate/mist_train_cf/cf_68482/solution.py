"""
QUESTION:
Implement two functions, `count_term` and `compare_term`, to analyze the recurrence of a term in literary works.

The `count_term` function should take in a list of works (as strings) by a single writer and a term, and return the count of occurrences of that term in the writer's works, ignoring case sensitivity, punctuation, special characters, and white spaces.

The `compare_term` function should take in a dictionary where the keys are writer names and the values are lists of their works, and return a dictionary where the keys are the writer names and the values are the count of occurrences of the term in each writer's works.

Both functions should maintain efficiency even with substantial input size.
"""

import re
from collections import defaultdict

def count_term(writer_works, term):
    count = 0
    for work in writer_works:
        work = re.sub(r'\W+', ' ', work.lower())
        words = work.split()
        count += words.count(term.lower())
    return count

def compare_term(all_writers_works, term):
    count_dict = defaultdict(int)
    for writer, works in all_writers_works.items():
        count_dict[writer] = count_term(works, term)
    return dict(count_dict)