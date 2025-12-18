"""
QUESTION:
Create a function named `remove_elements` that takes a list of positive integers as input, removes all elements that occur more than three times, and returns the modified list sorted in descending order. The function should have a time complexity of O(n log n), where n is the length of the input list. The input list will contain at most 10^6 elements and will always contain at least one element.
"""

def remove_elements(lst):
    # Step 1: Count the occurrences of each element
    count = {}
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # Step 2: Remove elements that occur more than three times
    new_lst = []
    for num in lst:
        if count[num] <= 3:
            new_lst.append(num)

    # Step 3: Sort the new list in descending order
    new_lst.sort(reverse=True)

    return new_lst