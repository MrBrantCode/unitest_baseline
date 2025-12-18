"""
QUESTION:
Implement a function called `merge_sort` that takes a list of words as input and returns a list of unique words in alphabetical order without using any built-in sorting functions. The function should handle words containing both uppercase and lowercase letters, be case-insensitive, and remove any duplicate words. The function should have a time complexity of O(n log n).
"""

def merge_sort(words):
    words = [word.lower() for word in words]
    words = list(set(words))

    if len(words) <= 1:
        return words

    mid = len(words) // 2
    left_half = words[:mid]
    right_half = words[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    sorted_words = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            sorted_words.append(left_half[left_index])
            left_index += 1
        else:
            sorted_words.append(right_half[right_index])
            right_index += 1

    sorted_words.extend(left_half[left_index:])
    sorted_words.extend(right_half[right_index:])

    return sorted_words