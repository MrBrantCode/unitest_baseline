"""
QUESTION:
Write a function called `most_common` that finds the most common element in a given array. The array may contain duplicate elements, and there may be multiple elements with the same maximum frequency. In such cases, return any of the most common elements.
"""

def most_common(arr):
    counts = {}
    for i in arr:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    
    max_count = 0
    max_item = None
    for item, count in counts.items():
        if count > max_count:
            max_count = count
            max_item = item

    return max_item