"""
QUESTION:
Create a function named `odd_count_elements` that takes two lists as input and returns a list of elements that appear an odd number of times in the combined list. The output list should be sorted in descending order. The function should not use any built-in list operations for sorting or calculating the count of amalgamations.
"""

def odd_count_elements(list1, list2):
    counts = {}
    for i in list1 + list2:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    odds = [i for i in counts if counts[i] % 2 != 0]

    # Manually implementing a bubble sort since we can't use built-in sort functions
    for i in range(len(odds)):
        for j in range(len(odds) - 1):
            if odds[j] < odds[j + 1]:
                odds[j], odds[j + 1] = odds[j + 1], odds[j]

    return odds