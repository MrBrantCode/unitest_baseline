"""
QUESTION:
Implement a function `custom_sort` that sorts an array of strings based on their length in descending order. If two strings have the same length, they should be sorted lexicographically in descending order. The function should have a time complexity of O(n log n) and a space complexity of O(1).
"""

def custom_sort(arr):
    def compare_strings(s1, s2):
        if len(s1) != len(s2):
            return len(s2) - len(s1)
        else:
            return -1 if s1 > s2 else 1

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = custom_sort(arr[:mid])
    right_half = custom_sort(arr[mid:])
    
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if compare_strings(left_half[i], right_half[j]) < 0:
            arr[i + j] = left_half[i]
            i += 1
        else:
            arr[i + j] = right_half[j]
            j += 1
    
    while i < len(left_half):
        arr[i + j] = left_half[i]
        i += 1
    
    while j < len(right_half):
        arr[i + j] = right_half[j]
        j += 1
    
    return arr