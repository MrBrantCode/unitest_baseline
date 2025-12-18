"""
QUESTION:
Implement a function called `custom_sort` that takes two parameters: `integer_collection` and `word_collection`. The function should return two sorted lists. The `integer_collection` should be sorted in ascending order using a custom sorting algorithm with a time complexity better than O(N^2). The `word_collection` should be sorted in alphabetical order using a custom sorting algorithm with a time complexity better than O(N^2), ignoring vowels in the words during the sorting process.
"""

def remove_vowels(word):
    return ''.join(ch for ch in word if ch not in 'aeiou')

def merge_sort(lst, key=lambda x: x):
    if len(lst) < 2:
        return lst
    mid = len(lst)//2
    left = merge_sort(lst[:mid], key)
    right = merge_sort(lst[mid:], key)
    return merge(left, right, key)

def merge(left, right, key):
    result = []
    while left and right:
        if key(left[0]) <= key(right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right

def custom_sort(integer_collection, word_collection):
    integer_collection = merge_sort(integer_collection)
    word_collection = merge_sort(word_collection, key=remove_vowels)
    return integer_collection, word_collection