"""
QUESTION:
Find all shortest transformation sequences from `beginWord` to `endWord` using a dictionary `wordList`. Each word in the sequence must differ by a single letter from the previous word and must be in `wordList`. The transformation sequence should not contain any palindromic words.

Write a function `findLadders` that takes `beginWord`, `endWord`, and `wordList` as input and returns all the shortest transformation sequences from `beginWord` to `endWord`. If no such sequence exists, return an empty list.

Constraints:

* `1 <= beginWord.length <= 10`
* `endWord.length == beginWord.length`
* `1 <= wordList.length <= 5000`
* `wordList[i].length == beginWord.length`
* `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.
* `beginWord != endWord`
* All the words in `wordList` are unique.
* No word in `wordList` is a palindrome.
"""

def findLadders(beginWord, endWord, wordList):
    """
    This function finds all shortest transformation sequences from beginWord to endWord 
    using a dictionary wordList. Each word in the sequence must differ by a single 
    letter from the previous word and must be in wordList. The transformation sequence 
    should not contain any palindromic words.

    Args:
        beginWord (str): The starting word for the transformation.
        endWord (str): The target word for the transformation.
        wordList (list): A list of words that can be used in the transformation.

    Returns:
        list: A list of all shortest transformation sequences from beginWord to endWord.
    """

    def is_palindrome(word):
        return word == word[::-1]

    wordList = set(wordList)
    if endWord not in wordList or is_palindrome(beginWord) or is_palindrome(endWord):
        return []

    layer = {}
    layer[beginWord] = [[beginWord]]

    while layer:
        newlayer = {}
        for w in layer:
            if w == endWord: 
                return layer[w]
            for i in range(len(w)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    neww = w[:i]+c+w[i+1:]
                    if neww in wordList and not is_palindrome(neww):
                        if neww not in newlayer:
                            newlayer[neww] = []
                        newlayer[neww] += [j+[neww] for j in layer[w]]

        wordList -= set(newlayer.keys())
        layer = newlayer

    return []