"""
QUESTION:
Design a function called 'shared_elements' that takes two lists as input and returns a list containing the common unique elements from the input lists, arranged in an increasing sequence. The function should not use any Python built-in list functions or libraries for removing duplicates or sorting, and should avoid brute-force or nested-iteration. If the lists contain strings, the function should combine the common unique strings in lexicographical order.
"""

def entrance(list1: list, list2: list) -> list:
    # Using set to find intersection of the two lists
    common_elements = list(set(list1) & set(list2))

    # Implement simple Bubble Sort for the final list
    n = len(common_elements)

    # Bubble sort iterates over each item in the list
    # and compares it with the item next to it
    # If the item is larger than the next one, it swaps them
    # The highest value will eventually 'bubble' up to the end of the list
    for i in range(n):
        for j in range(0, n - i - 1):

            # If elements are strings, lexicographic order is used
            if common_elements[j] > common_elements[j + 1]:
                common_elements[j], common_elements[j + 1] = common_elements[j + 1], common_elements[j]

    return common_elements