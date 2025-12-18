"""
QUESTION:
Given a list of words followed by two words, the task to find the minimum distance between the given two words in the list of words
Example 1:
Input:
S = { "the", "quick", "brown", "fox", 
     "quick"}
word1 = "the"
word2 = "fox"
Output: 3
Explanation: Minimum distance between the 
words "the" and "fox" is 3
Example 2:
Input:
S = {"geeks", "for", "geeks", "contribute", 
     "practice"}
word1 = "geeks"
word2 = "practice"
Output: 2
Explanation: Minimum distance between the
words "geeks" and "practice" is 2
Your Task:  
You don't need to read input or print anything. Your task is to complete the function 
shortestDistance() which list of words, two strings as inputs and returns the minimum distance between two words
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)
Constraints:
Sum of lengths of words ≤ 10^{5}
Note: word1 and word2 are both in the list.
"""

def shortest_distance(words, word1, word2):
    if word1 == word2:
        return 0
    
    last_seen = {}
    min_distance = float('inf')
    
    for i, word in enumerate(words):
        if word == word1:
            if word2 in last_seen:
                min_distance = min(min_distance, i - last_seen[word2])
        elif word == word2:
            if word1 in last_seen:
                min_distance = min(min_distance, i - last_seen[word1])
        
        last_seen[word] = i
    
    return min_distance