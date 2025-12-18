"""
QUESTION:
Create a function `find_nth_smallest` that takes an integer `n` and an unsorted list of numbers as input, and returns the nth smallest number in the list. The function should have a time complexity of O(n log n) and a space complexity of O(1).
"""

def find_nth_smallest(n, numbers):
    def partition(numbers, low, high):
        pivot = numbers[high]
        i = low - 1

        for j in range(low, high):
            if numbers[j] <= pivot:
                i += 1
                numbers[i], numbers[j] = numbers[j], numbers[i]

        numbers[i + 1], numbers[high] = numbers[high], numbers[i + 1]
        return i + 1

    def quicksort(numbers, low, high):
        if low < high:
            pivot_index = partition(numbers, low, high)
            quicksort(numbers, low, pivot_index - 1)
            quicksort(numbers, pivot_index + 1, high)

    quicksort(numbers, 0, len(numbers) - 1)
    return numbers[n - 1]