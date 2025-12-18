"""
QUESTION:
Implement a function named `select_elements` that takes an array and an integer `k` as input. The function should select `k` non-consecutive, non-repeating, non-negative, and even elements from the array such that their sum is maximized. The function should have a time complexity of O(n), where n is the length of the array.
"""

def select_elements(arr, k):
    include = 0
    exclude = 0
    selected_elements = set()

    for i in range(len(arr)):
        new_include = max(include, exclude)
        include = arr[i] + exclude
        exclude = max(include, exclude)
        include = new_include

        if arr[i] % 2 == 1 or arr[i] < 0:
            i += 1
        elif arr[i] > 0 and arr[i] % 2 == 0 and arr[i] not in selected_elements:
            selected_elements.add(arr[i])
            if len(selected_elements) == k:
                break

    return sum(selected_elements)