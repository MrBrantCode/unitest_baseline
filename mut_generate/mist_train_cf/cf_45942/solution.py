"""
QUESTION:
Write a function `sort_even_indices_in_chunks` that takes a list `l` and an integer `k` as inputs. The function should return a new list that matches the original list on odd indices and has elements at even indices sorted in increasing order within chunks of size `k`. If the list of even-indexed elements cannot be divided into equal chunks of `k`, the remaining elements should also be sorted.
"""

def sort_even_indices_in_chunks(l: list, k: int):
    # Extract elements at even indices from list
    even_index_elements = [l[i] for i in range(0, len(l), 2)]

    # If there are elements, sort them in chunks of 'k'
    if even_index_elements:
        new_sorted_chunk = []

        # Loop over the list by step of 'k'
        for i in range(0, len(even_index_elements), k):
            # Sort the chunk and add it to the new_sorted_chunk list
            new_sorted_chunk += sorted(even_index_elements[i: i + k])

        # Insert sorted elements of new_sorted_chunk into the original list at even indices
        for i, val in enumerate(new_sorted_chunk):
            l[i * 2] = val

    return l