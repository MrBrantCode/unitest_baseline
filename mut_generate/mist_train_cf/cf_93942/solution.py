"""
QUESTION:
Create a function called mergeAndRemoveDuplicates that takes two arrays as input, merges them, removes duplicates, and returns the merged array sorted in ascending order. The function should meet the following requirements:
- Time Complexity: O(n log n), where n is the total number of elements in the merged array.
- Space Complexity: O(n), where n is the total number of elements in the merged array.
"""

def mergeAndRemoveDuplicates(arr1, arr2):
    merged = arr1 + arr2

    def mergeSort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])

        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            elif left[i] > right[j]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    mergedSorted = mergeSort(merged)

    result = []
    visitedSet = set()

    for num in mergedSorted:
        if num not in visitedSet:
            visitedSet.add(num)
            result.append(num)

    return result