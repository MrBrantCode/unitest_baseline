"""
QUESTION:
Write a function called `find_anagram_pairs` that takes an array of lowercase English words as input and returns a list of pairs of words that are anagrams of each other. The function should have a time complexity of O(n^2), where n is the length of the input array, and a space complexity of O(1), meaning no additional data structures can be used to store intermediate results. Each word in the input array can have at most 100 characters.
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