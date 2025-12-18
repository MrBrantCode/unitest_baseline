"""
QUESTION:
You are given an array of integers representing the frequency of each letter of the alphabet (a=0, b=1, ..., z=25). Write a function named `most_frequent_letter_with_vowel` that determines the letter that appears the most frequently and is immediately followed by a vowel in the alphabet. The function should take the frequency array as input and return the corresponding letter. Assume the input array may contain negative numbers.
"""

def most_frequent_letter_with_vowel(arr):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    max_freq = -1
    max_letter = None
    for i in range(len(arr)):
        if i < len(arr)-1 and chr(i+97) in vowels and (arr[i] > max_freq or (arr[i] == max_freq and (max_letter is None or i < ord(max_letter)-97))):
            max_freq = arr[i]
            max_letter = chr(i+97)
    return max_letter