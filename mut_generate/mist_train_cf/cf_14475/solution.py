"""
QUESTION:
Implement a function named `merge_sort` that takes an array of characters as input. The function should sort the array in ascending order while ignoring case sensitivity. The sorted array should have all the vowels (a, e, i, o, u) placed before the consonants. The sorting algorithm used should have a time complexity of O(n log n).
"""

def is_vowel(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return char.lower() in vowels

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    i = j = 0
    sorted_arr = []
    while i < len(left) and j < len(right):
        if (is_vowel(left[i]) and is_vowel(right[j])) or (not is_vowel(left[i]) and not is_vowel(right[j])):
            if left[i].lower() < right[j].lower():
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
        elif is_vowel(left[i]):
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr