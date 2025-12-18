"""
QUESTION:
Create a function `find_most_common` that takes a list of integers as input and returns the most common positive integer in the list, excluding duplicates. The function should ignore non-positive integers and return `None` if the list does not contain any positive integers.
"""

def find_most_common(lst):
    freq_count = {}
    for num in lst:
        if num > 0:
            if num not in freq_count:
                freq_count[num] = 1
            else:
                freq_count[num] += 1
    
    sorted_freq_count = sorted(freq_count.items(), key=lambda x: x[1], reverse=True)
    
    if sorted_freq_count:
        return sorted_freq_count[0][0]
    else:
        return None