"""
QUESTION:
Write a function `find_anagram_palindromes(words)` that takes a list of strings as input and returns a list of palindromic strings that are anagrams of each other. A palindromic string reads the same backward as forward and an anagram is a word or phrase formed by rearranging the letters of another word or phrase. The function should return all pairs of anagram palindromes from the input list. The input list only contains lowercase English letters.
"""

def find_anagram_palindromes(words):
    result = []
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]) and is_palindrome(words[i]):
                result.extend([words[i], words[j]])
    return result

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    count = [0] * 26
    for i in range(len(word1)):
        count[ord(word1[i]) - ord('a')] += 1
        count[ord(word2[i]) - ord('a')] -= 1
    for i in range(len(count)):
        if count[i] != 0:
            return False
    return True

def is_palindrome(word):
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True