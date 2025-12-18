"""
QUESTION:
Implement the `sort_strings` function to sort a list of strings in alphabetical order using a divide-and-conquer approach. The input list may contain duplicate strings and special characters, and the output list should have no duplicates, with all special characters at the end. The function should achieve a time complexity of O(n log n) and a space complexity of O(n).
"""

def sort_strings(list_of_strings):
    # Remove duplicates
    unique_strings = list(set(list_of_strings))

    # Sort using merge sort
    def merge_sort(strings):
        if len(strings) <= 1:
            return strings

        mid = len(strings) // 2
        left_half = strings[:mid]
        right_half = strings[mid:]

        sorted_left = merge_sort(left_half)
        sorted_right = merge_sort(right_half)

        return merge(sorted_left, sorted_right)

    def merge(left, right):
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

    sorted_strings = merge_sort(unique_strings)

    # Move special characters to the end
    sorted_strings = [s for s in sorted_strings if not s.isalpha()] + [s for s in sorted_strings if s.isalpha()]

    return sorted_strings