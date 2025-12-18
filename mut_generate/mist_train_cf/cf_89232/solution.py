"""
QUESTION:
Implement a function named `quicksort` that takes an array of strings as input, where each string represents a sentence. Sort the sentences in ascending order based on the number of vowels in each sentence. If two sentences have the same number of vowels, sentences that start with a consonant should be placed before sentences that start with a vowel. The function should return the sorted array of sentences.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    less = []
    equal = []
    more = []

    for sentence in arr:
        vowel_count = sum(1 for char in sentence.lower() if char in 'aeiou')
        if vowel_count < sum(1 for char in pivot.lower() if char in 'aeiou'):
            less.append(sentence)
        elif vowel_count == sum(1 for char in pivot.lower() if char in 'aeiou'):
            if not sentence[0].isalpha() or sentence[0].lower() < pivot[0].lower():
                less.append(sentence)
            else:
                equal.append(sentence)
        else:
            more.append(sentence)

    return quicksort(less) + equal + quicksort(more)