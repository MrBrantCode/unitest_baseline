"""
QUESTION:
Write a function named `find_duplicates_recursive` that takes a list of integers as input and returns a list of integers. The function should find all elements that appear more than once in the given list, return them in ascending order, and remove any duplicate elements from the result. The function should be implemented recursively and without using any built-in functions or libraries. The input list will have a maximum length of 10^5.
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
    duplicates = find_duplicates(0, counts, [])
    
    return duplicates