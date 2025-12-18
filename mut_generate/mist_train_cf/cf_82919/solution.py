"""
QUESTION:
Create a function `count_and_sort(arr)` that takes a list of integers as input, removes duplicates, sorts the unique elements in ascending order, and returns the sorted list along with a dictionary where the keys are the unique elements and the values are their respective counts in the original list.
"""

def count_and_sort(arr):
    #create a dictionary to store count
    counter = {}
    for num in arr:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    #sort and remove duplicates
    unique_arr = sorted(list(counter.keys()))

    return unique_arr, counter