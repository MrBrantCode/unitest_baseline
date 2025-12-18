"""
QUESTION:
Write a function `find_duplicates(lst)` that takes a list `lst` as input and returns a list of duplicate elements in the order they first appear in the input list. The function should have a time complexity of O(n), where n is the number of elements in the input list.
"""

def find_duplicates(lst):
    duplicates = []
    freq = {}
    for i in lst:
        if i in freq:
            if freq[i] == 1:
                duplicates.append(i)
            freq[i] += 1
        else:
            freq[i] = 1
    return duplicates