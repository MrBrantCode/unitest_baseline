"""
QUESTION:
Given a list of words `wordList` and two words `beginWord` and `endWord`, determine the length of the shortest transformation sequence from `beginWord` to `endWord` using only words from `wordList`, where each word in the sequence must differ by exactly one character. The function `shortestTransformationLength` should take in the `wordList`, `beginWord`, and `endWord` as input and return the length of the shortest transformation sequence. If no such transformation sequence exists, return 0.
"""

from collections import deque

def shortestTransformationLength(wordList, beginWord, endWord):
    wordList = set(wordList)
    queue = deque([(beginWord, 1)])
    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordList:
                    wordList.remove(next_word)
                    queue.append((next_word, length + 1))
    return 0