"""
QUESTION:
Given an array of unique lowercase English words, write a function `palindromePairs` to find all pairs of distinct indices `(i, j)` such that the concatenation of the two words, `words[i] + words[j]`, forms a palindrome.

The input array `words` has a length ranging from 1 to 5000, inclusive, and each word `words[i]` has a length ranging from 1 to 20, inclusive. The function should return a list of pairs of indices that form palindrome pairs.

The function should be efficient in terms of time complexity, using a hash map or similar data structure to store and lookup reversed words. The algorithm should check all possible prefixes and postfixes of each word to determine if they form a palindrome pair.
"""

def palindromePairs(words):
	revWords = {w[::-1]: i for i, w in enumerate(words)}
	result = []
	for i, word in enumerate(words):
		for j in range(len(word)+1):
			prefix, postfix = word[:j], word[j:]
			if prefix == prefix[::-1] and revWords.get(postfix, -1) != -1 and revWords[postfix] != i:
				result.append([revWords[postfix], i])
			if j != len(word) and postfix == postfix[::-1] and revWords.get(prefix, -1) != -1 and revWords[prefix] != i:
				result.append([i, revWords[prefix]])
	return result