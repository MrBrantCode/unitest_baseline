"""
QUESTION:
Write a function `main` that calculates the sum of the maximum and minimum integers in a nested list. The function should be able to handle nested lists of arbitrary depth. The function should return the sum of the maximum and minimum integers in the list.
"""

def main(lst):
    def flatten(lst):
        flat_list = []
        for e in lst:
            if type(e) is list:
                flat_list.extend(flatten(e))
            else:
                flat_list.append(e)
        return flat_list

    flat_list = flatten(lst)
    return max(flat_list) + min(flat_list)