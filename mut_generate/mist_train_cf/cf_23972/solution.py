"""
QUESTION:
Implement the function `sort_list(numbers)` that takes a list of numbers as input and returns the sorted list in ascending order. The input list contains only integers and may be unsorted, empty, or already sorted. The function should modify the original list and return the sorted list.
"""

def sort_list(numbers):
    for i in range(len(numbers)):
        min_idx = i
        for j in range(i+1, len(numbers)):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers