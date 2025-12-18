"""
QUESTION:
Create a function called `mostFreqPalindromeSubstring` that takes a string `seq` as input and returns the frequency of the most frequently occurring palindromic substring within `seq`. Use a trie data structure to solve this problem. Assume that the input string only contains characters that can be compared for equality and that the function should be able to handle strings of any length.
"""

class TrieNode: 
    def __init__(self): 
        self.count = 0
        self.children = {} 

class Trie: 
    def __init__(self): 
        self.root = TrieNode()
        
    def insert(self, word): 
        node = self.root 
        for i, char in enumerate(reversed(word)): 
            if char not in node.children: 
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

    def find(self, word): 
        node = self.root 
        for i, char in enumerate(reversed(word)): 
            if char not in node.children: 
                return 0
            node = node.children[char]
        return node.count 

    def palindromeSubstrings(self, s): 
        result = 0
        for i in range(len(s)): 
            even_palindrome = self.find(s[i:]) 
            odd_palindrome = self.find(s[i + 1:]) 
            result += even_palindrome + odd_palindrome
        return result 

def mostFreqPalindromeSubstring(seq): 
    trie = Trie() 
    subStrings = [seq[i: j] for i in range(len(seq)) for j in range(i + 1, len(seq) + 1)] 
    for subString in subStrings: 
        trie.insert(subString) 
        
    return trie.palindromeSubstrings(seq)