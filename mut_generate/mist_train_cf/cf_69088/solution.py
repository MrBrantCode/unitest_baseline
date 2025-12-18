"""
QUESTION:
Create a function named correct_sort that sorts a list of numbers in ascending order without using Python's built-in sort function. The function should take a list of numbers as input and return the sorted list. The function should use a comparison-based algorithm, specifically bubble sort, to sort the list.
"""

def correct_sort(numbers):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers