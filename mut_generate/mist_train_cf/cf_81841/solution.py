"""
QUESTION:
Create a function named `merge_and_sort` that takes two lists of positive integers as input, merges them, sorts the combined list in descending order, and returns the sorted list with no digit appearing more than twice. If a digit appears more than twice, keep the two largest occurrences and remove the rest.
"""

def merge_and_sort(list1, list2):
    # Merge the lists
    merged = list1 + list2

    # Sort the list in descending order
    merged.sort(reverse=True)

    # Create a dictionary to keep track of the frequency of each number
    freq = {}

    # Iterate over the list
    for num in merged:
        # If the number is not in the dictionary, add it with count 1
        if num not in freq:
            freq[num] = 1
        # If the number is already in the dictionary and its count is less than 2, increase the count
        elif freq[num] < 2:
            freq[num] += 1

    # Create a new list to keep the final result
    result = []

    # Iterate over the list again
    for num in merged:
        # If the count of the number is greater than 0, append it to the result and decrease the count
        if freq[num] > 0:
            result.append(num)
            freq[num] -= 1

    return result