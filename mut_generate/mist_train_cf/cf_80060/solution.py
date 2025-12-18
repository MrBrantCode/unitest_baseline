"""
QUESTION:
Implement a function named `bubble_sort` that sorts a given list in-place using the bubble sort algorithm, meeting a space complexity of O(1). The function should also return the number of swaps made during the sorting process. The input list is a list of integers, and the output should be the sorted list and the number of swaps. Additionally, implement a check to confirm if the list is indeed sorted on completion.
"""

def bubble_sort(numbers):
    swaps = 0
    list_len = len(numbers)
    for i in range(list_len):
        for j in range(0, list_len - i - 1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swaps += 1
    return numbers, swaps