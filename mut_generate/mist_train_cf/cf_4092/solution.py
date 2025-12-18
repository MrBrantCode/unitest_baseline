"""
QUESTION:
Write a function named `most_frequent_item` that takes a list of integers as input and returns the most frequent item. If there are multiple items with the same highest frequency, return the item that appears first in the list. The function should have a time complexity of O(n), where n is the length of the input list, and should not use any built-in Python functions for counting occurrences or finding the most frequent item, nor any additional data structures such as dictionaries or sets to store intermediate results or counts.
"""

def most_frequent_item(lst):
    max_count = 0
    max_item = None

    # iterate through the list
    for i in range(len(lst)):
        count = 0

        # count occurrences of the current item in the list
        for j in range(len(lst)):
            if lst[j] == lst[i]:
                count += 1

        # check if the current item has higher frequency than the current maximum
        if count > max_count:
            max_count = count
            max_item = lst[i]

        # if the current item has the same frequency as the current maximum,
        # update max_item only if it appears earlier in the list
        elif count == max_count and lst.index(lst[i]) < lst.index(max_item):
            max_item = lst[i]

    return max_item