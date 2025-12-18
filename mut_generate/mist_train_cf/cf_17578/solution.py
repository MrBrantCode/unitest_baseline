"""
QUESTION:
Write a function named `find_subsets` that takes a string and returns all possible subsets of the string, including the empty string. The function should not take any additional parameters other than the string and should not return anything, but instead print all subsets.
"""

def find_subsets(string, current_subset="", index=0):
    if index == len(string):
        print(current_subset)
        return

    find_subsets(string, current_subset + string[index], index + 1)
    find_subsets(string, current_subset, index + 1)