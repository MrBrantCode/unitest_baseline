"""
QUESTION:
Implement the function `categorize_words(words)` to categorize the input list of words into groups based on the number of unique vowels in each word, ignoring vowels that appear more than once in a word. The function should return a dictionary where the keys are the number of unique vowels and the values are lists of words with that number of unique vowels. The time complexity of the solution should be O(n), where n is the number of words in the input list.
"""

def categorize_words(words):
    result = {}
    for word in words:
        unique_vowels = set()
        for char in word:
            if char.lower() in {'a', 'e', 'i', 'o', 'u'}:
                unique_vowels.add(char.lower())
        if len(unique_vowels) > 1:
            continue
        elif len(unique_vowels) == 1:
            num_unique_vowels = len(unique_vowels)
            if num_unique_vowels not in result:
                result[num_unique_vowels] = []
            result[num_unique_vowels].append(word)
    return result