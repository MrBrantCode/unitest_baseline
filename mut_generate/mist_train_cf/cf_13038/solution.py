"""
QUESTION:
Implement a QuickSort algorithm using the function `quickSort(sentences, left, right)` to sort an array of strings (sentences) in ascending order based on the number of vowels in each sentence. The function `countVowels(sentence)` should be used as a helper function to count the number of vowels in a sentence. Assume the input array is not empty and the sentences are case-insensitive.
"""

def countVowels(sentence):
    count = 0
    sentence = sentence.lower()
    for char in sentence:
        if char in 'aeiou':
            count += 1
    return count

def quickSort(sentences, left, right):
    if left < right:
        pivot = countVowels(sentences[right])
        i = left
        j = right - 1
        while i <= j:
            while i <= j and countVowels(sentences[i]) <= pivot:
                i += 1
            while i <= j and countVowels(sentences[j]) > pivot:
                j -= 1
            if i <= j:
                sentences[i], sentences[j] = sentences[j], sentences[i]
                i += 1
                j -= 1
        sentences[i], sentences[right] = sentences[right], sentences[i]
        quickSort(sentences, left, i - 1)
        quickSort(sentences, i + 1, right)
    return sentences