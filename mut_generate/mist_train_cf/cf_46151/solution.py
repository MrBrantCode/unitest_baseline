"""
QUESTION:
Write a function `penultimate_greatest_in_range` that takes a list of numbers and a range as input, and returns the second greatest number in the list that falls within the given range. If there is no second greatest number (i.e., less than two numbers in the list fall within the range), return None. The range is inclusive.
"""

def penultimate_greatest_in_range(lst, range_):
    filtered = [x for x in lst if range_[0] <= x <= range_[1]]
    filtered = list(set(filtered))
    filtered.sort(reverse=True)
    return filtered[1] if len(filtered) >= 2 else None