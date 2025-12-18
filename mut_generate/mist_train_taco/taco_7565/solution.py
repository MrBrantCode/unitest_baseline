"""
QUESTION:
Given a string S, check if it is possible to convert it into a string that is the repetition of a substring with K characters. To convert, we can replace one substring of length K starting at index i (zero-based indexing), such that i is divisible by K, with K characters.
Example 1:
Input:
N = 4, K = 2, S = "bdac"
Output: 1
Explanation: We can replace either
"bd" with "ac" or "ac" with "bd"
Example 2:
Input: 
N = 5, K = 2, S = "abcde"
Output: 0
Explanation: Since N % K != 0, it's not 
possible to convert S into a string which
is a concatanation of a substring with 
length K.
Your Task:
You don't need to read input or print anything. Your task is to complete the function kSubstrConcat() which takes a string S, its length N and an integer K as inputs and return 1/0 accordingly.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
2 <= K < N <= 100000
"""

def can_form_k_repeated_substring(S, N, K):
    if N % K != 0:
        return 0
    
    pat = S[0:K]
    (cnt, cnt2) = (0, 0)
    pat2 = ''
    
    for i in range(0, N, K):
        if pat == S[i:i + K]:
            cnt += 1
        elif pat2 == '':
            pat2 = S[i:i + K]
            cnt2 += 1
        elif pat2 == S[i:i + K]:
            cnt2 += 1
    
    if (cnt <= 1 or cnt2 <= 1) and cnt + cnt2 == N // K:
        return 1
    
    return 0