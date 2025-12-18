"""
QUESTION:
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.
Example 1:
Input: d = {"ale", "apple", "monkey", "plea"}
       S = "abpcplea"
Output: "apple" 
Explanation: After deleting "b", "c"
"a" S became "apple" which is present
in d.
Example 2:
Input: d = {"a", "b", "c"}
       S = "abpcplea"
Output: "a"
Explanation: After deleting "b", "p"
"c", "p", "l", "e", "a" S became 
"a" which is present in d.
Your Task:  
You dont need to read input or print anything. Complete the function findLongestWord() which takes S and d as input parameter and returns the longest word.
Expected Time Complexity: O(n*x)
Expected Auxiliary Space: O(x)
Constraints:
1 ≤ n,x ≤ 10^{3}
"""

def find_longest_word(S, d):
    def can_form_word(word, S):
        i = j = 0
        while i < len(S) and j < len(word):
            if word[j] == S[i]:
                j += 1
            i += 1
        return j == len(word)

    longest_word = ""
    for word in sorted(d):
        if can_form_word(word, S):
            if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
                longest_word = word
    return longest_word