"""
QUESTION:
Write a function named `count_unique_words` that takes a sentence as input and returns the number of unique words that start and end with a vowel (considering both lowercase and uppercase vowels) and do not contain a vowel followed immediately by a consonant. The function should have a time complexity less than O(n^2), where n is the total number of characters in the sentence.
"""

def count_unique_words(sentence):
    """
    Returns the number of unique words in a sentence that start and end with a vowel
    (considering both lowercase and uppercase vowels) and do not contain a vowel 
    followed immediately by a consonant.

    Time complexity: O(n), where n is the total number of characters in the sentence.
    """
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    unique_words = set()
    
    words = sentence.split()
    
    for word in words:
        if len(word) > 2 and word[0] in vowels and word[-1] in vowels:
            has_adjacent_consonant = False
            for i in range(len(word) - 1):
                if word[i] in vowels and word[i+1] not in vowels:
                    has_adjacent_consonant = True
                    break
            if not has_adjacent_consonant:
                unique_words.add(word.lower())
    
    return len(unique_words)