"""
QUESTION:
Create a function named `flatten` that takes a nested list as input and returns a new list that is the result of the following operations: 
- Flatten the nested list to a one-dimensional list
- Remove any duplicate elements
- Sort the remaining elements in descending order
"""

def flatten(nested_list):
    flat_list = []

    def recursive_flatten(lst):
        for i in lst:
            if type(i) == list:
                recursive_flatten(i)
            else:
                flat_list.append(i)

    recursive_flatten(nested_list)

    # remove duplicates using the set data structure
    no_duplicates_list = list(set(flat_list))

    # sort in descending order
    sorted_list = sorted(no_duplicates_list, reverse=True)

    return sorted_list