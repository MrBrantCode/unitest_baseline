"""
QUESTION:
Create a function named `categorize_words` that takes a list of words as input and returns a dictionary where the keys are the number of vowels in each word and the values are lists of words with that number of vowels. The input list can contain duplicates and the order of the words in each list does not matter. The function should be efficient and avoid unnecessary memory usage.
"""

def categorize_words(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = {}

    for word in words:
        count = sum(1 for char in word.lower() if char in vowels)
        if count not in result:
            result[count] = []
        result[count].append(word)

    return result