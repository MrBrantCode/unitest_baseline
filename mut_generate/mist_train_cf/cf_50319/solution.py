"""
QUESTION:
Implement a function `most_common(set1, set2)` that takes two lists of elements as input and returns the most common elements across both sets along with their frequencies. The solution should have a time complexity not exceeding O(n+m) and a space complexity not exceeding O(n+m), where n and m are the sizes of the two input sets.
"""

from collections import Counter

def most_common(set1, set2):
    counter1 = Counter(set1)
    counter2 = Counter(set2)
    combined_counter = counter1 + counter2
    common_elements = [i for i in combined_counter.keys() if i in counter1 and i in counter2]
    most_common_elements = Counter({i: combined_counter[i] for i in common_elements}).most_common()
    return most_common_elements