"""
QUESTION:
Create a function called `remove_elements` that takes a list of positive integers as input. The function should remove all elements that occur more than three times from the input list, sort the remaining elements in descending order, and return the modified list. The function should have a time complexity of O(n log n), where n is the length of the input list.
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