"""
QUESTION:
Write a function called `most_frequent_letter_with_vowel` that takes an array of integers representing the frequency of letters in a text, where each index in the array corresponds to a letter of the alphabet (0-based index, where 'a' is at index 0, 'b' is at index 1, and so on). The function should return the letter that appears most frequently in the text and is followed by a vowel. If no such letter exists, return None. The input array may contain negative numbers.
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