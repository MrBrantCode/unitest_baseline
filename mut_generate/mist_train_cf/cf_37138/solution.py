"""
QUESTION:
Create a function `filterAndSortSequences(bookId, sequences)` that takes an integer `bookId` and a list of tuples `sequences` as input, where each tuple contains a book ID and a sequence number. The function should return a list of sequence numbers in ascending order that correspond to the given `bookId`.
"""

def filter_and_sort_sequences(bookId, sequences):
    filtered_sequences = [sequence[1] for sequence in sequences if sequence[0] == bookId]
    filtered_sequences.sort()
    return filtered_sequences