"""
QUESTION:
Implement a function `compute_word_sums(words)` that takes an array of words, replaces each character with its corresponding number from the English alphabet, and finds the computed sum. The function must handle words containing uppercase letters, special characters, or numbers by converting them to lowercase and ignoring special characters and numbers, respectively. The function should return the array of words sorted in ascending order based on their computed sums with a time complexity of O(n log n), where n is the length of the array. The length of the array will be at most 100, and each word will have at most 10 characters.
"""

def get_word_sum(word):
    word_sum = 0
    for char in word:
        if char.isalpha():
            word_sum += ord(char.lower()) - ord('a') + 1
    return word_sum

def compute_word_sums(words):
    words_lower = [word.lower() for word in words]
    return sorted(words_lower, key=get_word_sum)