"""
QUESTION:
Trie is an efficient information retrieval data structure. Use this data structure to store Strings and search strings. Your task is to use TRIE data structure and search the given string A. If found print 1 else 0.
Example 1:
Input:
N = 8
key[] = {the,a,there,answer,any,by,
         bye,their}
search = the
Output: 1
Explanation: the is present in the given
string "the a there answer any by bye
their"
Example 2:
Input:
N = 8
key[] = {the,a,there,answer,any,by,
         bye,their}
search = geeks
Output: 0
Explanation: geeks is not present in the
given string "the a there answer any by
bye their"
Your Task:
Complete insert and search function and return true if key is present in the formed trie else false in the search function. (In case of true, 1 is printed and false, 0 is printed by the driver's code.
Expected Time Complexity: O(M+|search|).
Expected Auxiliary Space: O(M).
M = sum of the length of all strings which is present in the key[] 
|search| denotes the length of the string search.
Constraints:
1 <= N <= 10^{4}
1 <= |input strings|, |A| <= 100
"""

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

def insert(root, key):
    curr = root
    for char in key:
        index = ord(char) - ord('a')
        if curr.children[index] is None:
            curr.children[index] = TrieNode()
        curr = curr.children[index]
    curr.isEndOfWord = True

def search(root, key):
    curr = root
    for char in key:
        index = ord(char) - ord('a')
        if curr.children[index] is None:
            return False
        curr = curr.children[index]
    return curr.isEndOfWord

def trie_search(keys, search_key):
    root = TrieNode()
    
    # Insert all keys into the Trie
    for key in keys:
        insert(root, key)
    
    # Search for the search_key in the Trie
    if search(root, search_key):
        return 1
    else:
        return 0