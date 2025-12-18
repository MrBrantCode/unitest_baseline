"""
QUESTION:
Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Examples:

Non-string inputs should be converted to strings.

Return an array of arrays containing pairs of distinct indices that form palindromes. Pairs should be returned in the order they appear in the original list.
"""

def find_palindrome_pairs(words):
    # Convert all elements to strings
    words = [str(word) for word in words]
    
    # Find all pairs of distinct indices (i, j) such that words[i] + words[j] is a palindrome
    palindrome_pairs = [[i, j] for i in range(len(words)) for j in range(len(words)) 
                        if words[i] + words[j] == (words[i] + words[j])[::-1] and i != j]
    
    return palindrome_pairs