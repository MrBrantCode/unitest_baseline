"""
QUESTION:
Write a function named `extract_regions` that takes a sequence of integers `seq`, an integer `threshold`, and an integer `tolerance` as input, and returns a list of lists, where each inner list represents a contiguous subsequence of `seq` that meets the following conditions:
- The subsequence consists of at least two consecutive integers.
- The absolute difference between any two adjacent integers in the subsequence is less than or equal to `tolerance`.
- The absolute difference between the maximum and minimum values in the subsequence is greater than or equal to `threshold`.
"""

def extract_regions(seq, threshold, tolerance):
    regions = []
    curr_region = []
    for i in range(len(seq)):
        if i == 0 or abs(seq[i] - seq[i-1]) <= tolerance:
            curr_region.append(seq[i])
        else:
            if len(curr_region) >= 2 and abs(max(curr_region) - min(curr_region)) >= threshold:
                regions.append(curr_region)
            curr_region = [seq[i]]
    if len(curr_region) >= 2 and abs(max(curr_region) - min(curr_region)) >= threshold:
        regions.append(curr_region)
    return regions