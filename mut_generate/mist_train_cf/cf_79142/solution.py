"""
QUESTION:
Write a function named `count_vowels` that takes a word as input and returns the number of vowels in the word. Then, use this function to sort a given list of words alphabetically and print each word along with its vowel count. The input list of words is ["dinosaur", "cat", "dog", "elephant", "tiger"]. The output should be in the format 'word: vowel count'.
"""

def count_vowels(word):
    count = 0
    for char in word:
        if char.lower() in 'aeiou':
            count += 1
    return count