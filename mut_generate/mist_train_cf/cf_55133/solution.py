"""
QUESTION:
Write a function named `check_array` that accepts a 2D array of words. The function should find the word with the longest length from each sub-array and check if that word contains the vowel 'e' in its second character position and in its penultimate character position. The function should return True if such a word is found in at least one sub-array, and False otherwise. Implement this without using any inbuilt Python functions.
"""

def check_array(arr):
    for sub_array in arr:
        if not sub_array:
            continue
        max_len = len(sub_array[0])
        max_word = sub_array[0]
        for word in sub_array:
            if len(word) > max_len:
                max_len = len(word)
                max_word = word
        if len(max_word) >= 2 and max_word[1] == 'e' and max_word[-2] == 'e':
            return True
    return False