"""
QUESTION:
Given two strings S1 and S2 in lowercase, the task is to make them anagram. The only allowed operation is to remove a character from any string. Find the minimum number of characters to be deleted to make both the strings anagram. Two strings are called anagram of each other if one of them can be converted into another by rearranging its letters.
Example 1:
Input:
S1 = bcadeh
S2 = hea
Output: 3
Explanation: We need to remove b, c
and d from S1.
Example 2:
Input:
S1 = cddgk
S2 = gcd
Output: 2
Explanation: We need to remove d and
k from S1.
Your Task:
Complete the function remAnagram() which takes two strings S1, S2 as input parameter, and returns minimum characters needs to be deleted.
Expected Time Complexity: O(max(|S1|, |S2|)), where |S| = length of string S.
Expected Auxiliary Space: O(26)
Constraints:
1 <= |S1|, |S2| <= 10^{5}
"""

def min_deletions_to_anagram(S1: str, S2: str) -> int:
    count_s1 = {}
    count_s2 = {}
    
    # Count frequency of each character in S1
    for char in S1:
        count_s1[char] = count_s1.get(char, 0) + 1
    
    # Count frequency of each character in S2
    for char in S2:
        count_s2[char] = count_s2.get(char, 0) + 1
    
    deletions = 0
    
    # Calculate the total deletions required
    for char in 'abcdefghijklmnopqrstuvwxyz':
        count1 = count_s1.get(char, 0)
        count2 = count_s2.get(char, 0)
        deletions += abs(count1 - count2)
    
    return deletions