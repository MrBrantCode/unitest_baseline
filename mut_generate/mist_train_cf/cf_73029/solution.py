"""
QUESTION:
Create a function `ladderLength(beginWord, endWord, wordList)` that returns the length of the shortest transformation sequence from `beginWord` to `endWord` using the words in `wordList`. If no such sequence exists, return 0. The sequence should be a list of words where each word differs by a single letter and all words in the sequence are in `wordList`. 

The function takes three parameters: `beginWord`, `endWord`, and `wordList`. `beginWord` and `endWord` are two strings of the same length, and `wordList` is a list of unique strings of the same length as `beginWord` and `endWord`. All strings consist of lowercase English letters.

Restrictions: `1 <= beginWord.length <= 10`, `endWord.length == beginWord.length`, `1 <= wordList.length <= 5000`, `wordList[i].length == beginWord.length`, `beginWord != endWord`.
"""

import collections

def ladderLength(beginWord, endWord, wordList):
    wordList = set(wordList)
    queue = collections.deque([[beginWord, 1]])
    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordList:
                    wordList.remove(next_word)
                    queue.append([next_word, length + 1])
    return 0