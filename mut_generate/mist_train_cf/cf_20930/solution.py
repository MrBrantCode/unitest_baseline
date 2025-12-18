"""
QUESTION:
Write a function `find_duplicates_recursive` that takes an array of integers as input, and returns an array of integers that appear more than once in the input array. The returned array should contain unique elements in ascending order. Implement the function recursively without using any built-in functions or libraries. The input array can have a maximum length of 10^5.
"""

def find_duplicates_recursive(arr):
    def count_elements(index, counts):
        if index == len(arr):
            return counts
        element = arr[index]
        counts[element] = counts.get(element, 0) + 1
        return count_elements(index + 1, counts)

    def find_duplicates(index, counts, duplicates):
        if index == len(arr):
            return sorted(duplicates)
        element = arr[index]
        if counts[element] > 1 and element not in duplicates:
            duplicates.append(element)
        return find_duplicates(index + 1, counts, duplicates)

    counts = count_elements(0, {})
    return find_duplicates(0, counts, [])