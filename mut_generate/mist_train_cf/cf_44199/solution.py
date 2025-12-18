"""
QUESTION:
Implement a function `merge_sort(data)` that takes a list of mixed graphic-symbols as input and returns the sorted list in ascending ASCII value order. Use the Merge Sort algorithm and handle both single-character elements and lists of characters. Note that the function should be case-sensitive and consider ASCII values of all characters, including alphabets, digits, and special characters.
"""

def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
          
        # Iterator for the main list
        k = 0
          
        while i < len(left_half) and j < len(right_half):
            if ord(left_half[i]) < ord(right_half[j]):
              # The value from the left_half has been used
              data[k] = left_half[i]
              # Move the iterator forward
              i += 1
            else:
                data[k] = right_half[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

    return data