"""
QUESTION:
Given a string S, consisting of lowercase Latin characters [a-z]. Find out all the possible palindromes that can be generated using the letters of the string and print them in lexicographical order.
Example 1:
Input: S = abbab
Output:{ abbba babab }
Explanation: abbba and babab are two
possible string whoch are palindrome.
Example 2:
Input: S = abc
Output: {}
Explanation: No permutation is palindromic.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function all_palindromes() which takes string S as the input parameter and returns a list of strings which are palindrome in lexicographical order.
 
Expected Time Complexity: O(2^n)
Expected Space Complexity: O(2^n)
 
Constraints:
1 <= Length of string <= 20
"""

def generate_palindromes(s: str) -> list[str]:
    def solve(cnt, k, n, curr):
        if k == n // 2:
            ans.append(''.join(curr))
            return
        for i in range(26):
            if cnt[i] >= 2:
                curr[k] = chr(ord('a') + i)
                curr[n - 1 - k] = curr[k]
                cnt[i] -= 2
                solve(cnt, k + 1, n, curr)
                cnt[i] += 2

    cnt = [0] * 26
    for c in s:
        cnt[ord(c) - ord('a')] += 1
    
    odd = 0
    c = ' '
    for i in range(26):
        if cnt[i] % 2 == 1:
            odd += 1
            c = chr(ord('a') + i)
    
    if odd > 1:
        return []
    
    ans = []
    n = len(s)
    curr = [' '] * n
    
    if odd == 1:
        curr[n // 2] = c
    
    solve(cnt, 0, n, curr)
    return ans