"""
QUESTION:
Write a function named `remove_singular_duplicates` that takes a list of strings as input and returns a new list where non-repeating string elements are removed and the order of the original elements is preserved. The function should be efficient and optimized for handling large data sets.
"""

def remove_singular_duplicates(mylist):
    count = {}
    result = []

    for s in mylist:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
        if count[s] == 1:
            result.append(s)

    return [s for s in result if count[s] > 1]