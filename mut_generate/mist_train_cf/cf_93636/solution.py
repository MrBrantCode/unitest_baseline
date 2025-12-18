"""
QUESTION:
Implement the function `merge_sort_descending(lst)` to sort a list of integers in descending order. The list may contain duplicates and have a length of up to 10^6. The function should use O(1) extra space and run in O(n log n) time complexity, where n is the length of the list. Additionally, it should remove any duplicate elements from the sorted list before returning the final result.
"""

def merge_sort_descending(lst):
    def merge(left, right):
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def remove_duplicates(lst):
        unique_lst = []
        last_seen = None
        for num in lst:
            if num != last_seen:
                unique_lst.append(num)
            last_seen = num
        return unique_lst

    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left_sorted = merge_sort_descending(left)
    right_sorted = merge_sort_descending(right)

    sorted_lst = merge(left_sorted, right_sorted)
    return remove_duplicates(sorted_lst)