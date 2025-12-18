"""
QUESTION:
Write a function `all_unique_permutations(arr)` that generates all unique permutations of a given list of numbers. The function should not use any built-in permutation functions and should handle repetitive numbers in the list.
"""

def all_unique_permutations(arr):
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def permutations(arr, start, end):
        result = set()
        if start == end:
            return [tuple(arr)]
        for i in range(start, end+1):
            if i != start and arr[i] == arr[start]:
                continue
            swap(arr, start, i)
            result.update(permutations(arr, start+1, end))
            swap(arr, start, i)    # Swap back to restore the original list
        return result

    return permutations(arr, 0, len(arr)-1)