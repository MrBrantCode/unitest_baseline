"""
QUESTION:
Write a function `most_frequent_letter_with_vowel(arr)` that takes an array of integers representing the frequency of letters in a text, where the index of each number corresponds to a letter in the alphabet (0=a, 1=b, 2=c, ..., 25=z). The function should return the letter that appears most frequently and is followed by a vowel (i.e., 'a', 'e', 'i', 'o', or 'u'). If no such letter exists, return None.
"""

def most_frequent_letter_with_vowel(arr):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    max_freq = -1
    max_letter = None
    for i in range(len(arr)):
        if arr[i] > max_freq and i < len(arr)-1 and chr(i+97) in vowels:
            max_freq = arr[i]
            max_letter = chr(i+97)
    return max_letter