"""
QUESTION:
Given a list of word lists of size  M * N. The task is to return all sentences possible taking one word from a list at a time via recursion. 
Example 1:
Input: 
L = {{"you", "we"},
     {"have", "are"},
Output: 
{{you have}
{you are}
{we have}
{we are}}
Explanation:
Consider every every word from the list and form
sentences with every other words, taking one word from a list .
Note: You need to maintain the order of the sentences.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function sentences() which takes a matrix of strings as input and returns a matrix of string containing all possible sentences.
Expected Time Complexity: O(M^{N})
Expected Auxiliary Space: O(M^{N})
 
Constraints:
1 <= M, N <= 6
'a' <= sentence[i][j] <= 'z'
"""

from typing import List

def generate_sentences(word_lists: List[List[str]]) -> List[List[str]]:
    ans = []

    def backtrack(i: int, curr: str):
        if i >= len(word_lists):
            ans.append(curr.strip().split())
            return
        for word in word_lists[i]:
            backtrack(i + 1, curr + ' ' + word)
    
    backtrack(0, '')
    return ans