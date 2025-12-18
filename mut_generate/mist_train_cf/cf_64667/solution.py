"""
QUESTION:
Return a list of the five least common elements in a given array using the function name `five_least_common`. The input array contains integers and the function should return a list of integers. The returned list should be ordered by the occurrence of each element in ascending order.
"""

from collections import Counter

def five_least_common(lst):
  # Count the occurrence of each element in the list
  counts = Counter(lst)
  # Get a list of the elements and their counts, sorted by count
  sorted_counts = sorted(counts.items(), key=lambda x: x[1])
  # Return the elements from the five least common
  return [element for element, count in sorted_counts[:5]]