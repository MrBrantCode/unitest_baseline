"""
QUESTION:
Create a function named `blend_words` that takes two string parameters and returns a new blended word. The blended word should contain at least two consecutive letters that appear in alphabetical order. The function should find the longest common substring between the two input words and blend them at that point. If no common substring is found, the function should return an empty string.
"""

def blend_words(word1, word2):
    for i in range(len(word1)):
        for j in range(len(word2)):
            if word1[i] == word2[j]:
                return word1[:i] + word2[j:]
            elif word1[i:i+2] in word2:
                return word1[:i] + word2[word2.index(word1[i:i+2]):]
            elif word2[j:j+2] in word1:
                return word2[:j] + word1[word1.index(word2[j:j+2]):]
    return ""