"""
QUESTION:
Write a function named `compare_pairs` that takes a list of pairs of numerical quantities (two-element arrays) as input and returns two values. The first value is a list where each element is a string ('subordinate', 'superior', or 'identical') based on the comparison of each pair. The second value is a dictionary with the count of each label in the first list.

The function should handle non-numeric elements in the input pairs by returning 'Invalid pair' for such pairs. The function should have optimal time and space complexity to handle large data sets efficiently.
"""

from collections import Counter, defaultdict

def compare_pairs(pairs):
    results = []
    counter_results = defaultdict(int)

    for pair in pairs:
        if all(isinstance(i, (int, float)) for i in pair):
            if pair[0] > pair[1]:
                results.append('superior')
            elif pair[0] < pair[1]:
                results.append('subordinate')
            else:
                results.append('identical')
        else:
            results.append('Invalid pair')

    counter_results = Counter(results)

    return results, dict(counter_results)