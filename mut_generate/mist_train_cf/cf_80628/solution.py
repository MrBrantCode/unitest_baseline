"""
QUESTION:
Create a function `reduce_list` that takes a list of elements as input. The list can contain integers, strings, or a combination of both. The function should return a list with a maximum of 5 distinct elements, dismissing the least frequent elements first. If two elements have the same frequency, the most recently added element should be dismissed first. Do not use in-built Python functions for sorting or the collections module, except for basic list operations.
"""

def reduce_list(lst):
    freq = {}  # Dictionary to track frequencies of elements.
    queue = []  # Queue to track order of elements.

    for element in lst:
        # If element already in dict, increase its count, otherwise add it to queue.
        if element in freq:
            freq[element] += 1
        else:
            queue.append(element)
            freq[element] = 1

        # If more than 5 distinct elements, dismiss the least frequent/most recent.
        while len(freq) > 5:
            dismissed = queue[0]
            freq[dismissed] -= 1
            # If count of dismissed element is 0, remove it from dict.
            if freq[dismissed] == 0:
                del freq[dismissed]
            queue.pop(0)

    return list(freq.keys())