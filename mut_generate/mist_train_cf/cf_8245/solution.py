"""
QUESTION:
Given a list of lowercase English words, find all pairs of words that are anagrams of each other. The function name should be `find_anagram_pairs` and it should take a list of strings `words` as input. The solution should have a time complexity of O(n^2), where n is the length of the input list, and a space complexity of O(1), without using any additional data structures to store intermediate results.
"""

def find_anagram_pairs(words):
    anagram_pairs = []
    n = len(words)
    
    for i in range(n):
        count1 = [0] * 26
        word1 = words[i]
        
        for char in word1:
            count1[ord(char) - ord('a')] += 1
        
        for j in range(i + 1, n):
            count2 = [0] * 26
            word2 = words[j]
            
            for char in word2:
                count2[ord(char) - ord('a')] += 1
            
            if count1 == count2:
                anagram_pairs.append((word1, word2))
    
    return anagram_pairs