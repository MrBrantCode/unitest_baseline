"""
QUESTION:
Create a function `positive_numbers_greater_than_10` that takes an array of integers as input and returns a new array containing only the positive numbers greater than 10, sorted in ascending order. The solution should not use any built-in Python functions or libraries for sorting and should have a time complexity of O(n log n).
"""

def positive_numbers_greater_than_10(arr):
    # Step 1: Filter out positive numbers greater than 10
    filtered_arr = [num for num in arr if num > 10]

    # Step 2: Sort the filtered array using merge sort algorithm
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

        return merge(left_half, right_half)

    def merge(left_half, right_half):
        merged_arr = []
        i = 0
        j = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                merged_arr.append(left_half[i])
                i += 1
            else:
                merged_arr.append(right_half[j])
                j += 1

        while i < len(left_half):
            merged_arr.append(left_half[i])
            i += 1

        while j < len(right_half):
            merged_arr.append(right_half[j])
            j += 1

        return merged_arr

    return merge_sort(filtered_arr)