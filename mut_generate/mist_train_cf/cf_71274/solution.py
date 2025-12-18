"""
QUESTION:
Implement the function `bubble_sort(sequence)` to sort a given sequence of unique whole numbers in ascending order using the bubble sort algorithm. The function should return the sorted sequence. The sequence can be of any length.
"""

def bubble_sort(sequence):
    index_length = len(sequence) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, index_length):
            if sequence[i] > sequence[i + 1]:
                sorted = False
                sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]

    return sequence