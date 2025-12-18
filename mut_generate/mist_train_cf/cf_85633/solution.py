"""
QUESTION:
Write a function named `sort_tuple` that takes a tuple of strings as input and returns a tuple of strings. The function should first filter out any strings with one or zero characters and then sort the remaining strings in ascending order based on their second last character. If the original tuple was already sorted according to this rule, the function should print "List is sorted." Otherwise, it should print "List was not sorted, but is now sorted." and return the sorted tuple.
"""

def sort_tuple(tup):
    error_free_list = [w for w in tup if isinstance(w, str) and len(w) > 1]
    sorted_tuple = tuple(sorted(error_free_list, key=lambda x: x[-2:]))
    if error_free_list == list(sorted_tuple):
        print("List is sorted.")
    else:
        print("List was not sorted, but is now sorted.")
    return sorted_tuple