"""
QUESTION:
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:


       Only one letter can be changed at a time.
       Each transformed word must exist in the word list. Note that beginWord is not a transformed word.


Note:


       Return 0 if there is no such transformation sequence.
       All words have the same length.
       All words contain only lowercase alphabetic characters.
       You may assume no duplicates in the word list.
       You may assume beginWord and endWord are non-empty and are not the same.


Example 1:


Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.


Example 2:


Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

def find_shortest_transformation_length(beginWord, endWord, wordList):
    wordDict = set(wordList)
    if endWord not in wordDict:
        return 0
    
    visited = set()
    beginSet = set([beginWord])
    visited.add(beginWord)
    endSet = set([endWord])
    visited.add(endWord)
    
    lenWord = len(beginWord)
    distance = 1
    
    while beginSet and endSet:
        if len(beginSet) > len(endSet):
            beginSet, endSet = endSet, beginSet
        
        newSet = set()
        for w in beginSet:
            for i in range(lenWord):
                part1 = w[:i]
                part2 = w[i + 1:]
                for alpha in 'abcdefghijklmnopqrstuvwxyz':
                    target = part1 + alpha + part2
                    if target in endSet:
                        return distance + 1
                    if target not in visited and target in wordDict:
                        newSet.add(target)
                        visited.add(target)
        
        beginSet = newSet
        distance += 1
    
    return 0