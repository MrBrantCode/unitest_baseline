"""
QUESTION:
Create a function `categorize_words` that takes a list of words as input and returns a dictionary where the keys are the number of vowels in each word and the values are lists of words with that number of vowels. The function should be efficient and handle input lists of up to 10^6 words with lengths of up to 10^3 characters, and the output dictionary should only include keys for numbers of vowels present in the input words.
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