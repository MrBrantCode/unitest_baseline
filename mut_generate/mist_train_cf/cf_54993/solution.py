"""
QUESTION:
Write a function named `five_least_common` that takes a list of integers as input and returns a list of the five least common elements in ascending order. If there are less than five distinct elements, return all distinct elements. If two or more elements have the same frequency, return them in ascending order of their values.
"""

def five_least_common(lst):
    counts = dict()
    
    for num in lst:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1
    
    least_common = sorted(counts.items(), key=lambda item: (item[1], item[0]))
    
    return [item[0] for item in least_common[:5]]