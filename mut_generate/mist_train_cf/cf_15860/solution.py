"""
QUESTION:
Implement the function `mergeAndRemoveDuplicates(arr1, arr2)` that merges two given arrays and removes duplicates. The merged array should be sorted in ascending order. The function should have a time complexity of O(n log n) and space complexity of O(n), where n is the total number of elements in the merged array.
"""

def mergeAndRemoveDuplicates(arr1, arr2):
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

    def removeDuplicates(arr):
        result = []
        visitedSet = set()

        for num in arr:
            if num not in visitedSet:
                visitedSet.add(num)
                result.append(num)

        return result

    merged = arr1 + arr2
    mergedSorted = mergeSort(merged)
    uniqueSorted = removeDuplicates(mergedSorted)
    return uniqueSorted