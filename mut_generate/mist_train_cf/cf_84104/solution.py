"""
QUESTION:
Write a function `find_most_frequent` that takes an array of n timestamps in "HH:MM" format as input and returns the timestamps with the highest frequency in ascending order along with a dictionary containing the frequency of each timestamp. The input array size is limited to 1 <= n <= 10^6. Optimize the solution for large inputs.
"""

from collections import Counter

def find_most_frequent(timestamps):
    counts = Counter(timestamps)
    max_count = max(counts.values())
    most_frequent = sorted(timestamp for timestamp, count in counts.items() if count == max_count)
    return most_frequent, counts