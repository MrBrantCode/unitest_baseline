"""
QUESTION:
Given an array of words, find all shortest unique prefixes to represent each word in the given array. Assume that no word is prefix of another.
Example 1:
Input: 
N = 4
arr[] = {"zebra", "dog", "duck", "dove"}
Output: z dog du dov
Explanation: 
z => zebra 
dog => dog 
duck => du 
dove => dov 
Example 2:
Input: 
N = 3
arr[] =  {"geeksgeeks", "geeksquiz",
                       "geeksforgeeks"};
Output: geeksg geeksq geeksf
Explanation: 
geeksgeeks => geeksg 
geeksquiz => geeksq 
geeksforgeeks => geeksf
Your task:
You don't have to read input or print anything. Your task is to complete the function findPrefixes() which takes the array of strings and it's size N as input and returns a list of shortest unique prefix for each word 
 
Expected Time Complexity: O(N*length of each word)
Expected Auxiliary Space: O(N*length of each word)
 
Constraints:
1 ≤ N, Length of each word ≤ 1000
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.freq = 0

class Solution:
    def insert(self, root, st):
        for i in range(len(st)):
            c = st[i]
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]
            root.freq += 1

    def get_prefix(self, root, st):
        pref = ''
        for i in range(len(st)):
            c = st[i]
            if root.freq == 1:
                break
            pref += c
            root = root.children[c]
        return pref

def find_shortest_unique_prefixes(arr, n):
    solution = Solution()
    root = TrieNode()
    for word in arr:
        solution.insert(root, word)
    ans = []
    for word in arr:
        ans.append(solution.get_prefix(root, word))
    return ans