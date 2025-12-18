"""
QUESTION:
Implement a function `merge_sort(arr)` that sorts a list of strings in alphabetical order using a divide-and-conquer approach. The function should handle lists with up to 10^6 strings efficiently, removing any duplicates and special characters, with a time complexity of O(n log n) and a space complexity of O(n).
"""

def merge_sort(arr):
    def merge(left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            elif left[i] > right[j]:
                result.append(right[j])
                j += 1
            else:  # removing duplicates
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

    if len(arr) <= 1:
        # Remove special characters and duplicates from input list
        arr = [''.join(e for e in s if e.isalnum()).lower() for s in arr]
        return list(set(arr))

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)