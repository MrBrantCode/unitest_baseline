"""
QUESTION:
Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that have exactly k distinct characters. 
Example 1:
Input:
S = "aba", K = 2
Output:
3
Explanation:
The substrings are:
"ab", "ba" and "aba".
Example 2:
Input: 
S = "abaaca", K = 1
Output:
7
Explanation:
The substrings are:
"a", "b", "a", "aa", "a", "c", "a". 
Your Task:
You don't need to read input or print anything. Your task is to complete the function substrCount() which takes the string S and an integer K as inputs and returns the number of substrings having exactly K distinct characters.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ |S| ≤ 10^{5}
1 ≤ K ≤ 26
"""

from collections import defaultdict, deque

def count_substrings_with_k_distinct_chars(s: str, k: int) -> int:
    def tempFunc(s, k):
        if k == 0:
            return 0
        result = 0
        mp = defaultdict(int)
        cnt = 0
        dq = deque()
        for i in s:
            if cnt == k and mp[i] == 0:
                while cnt == k:
                    mp[dq[0]] -= 1
                    if mp[dq[0]] == 0:
                        cnt -= 1
                    dq.popleft()
                mp[i] += 1
                cnt += 1
                dq.append(i)
                result += len(dq)
            else:
                if mp[i] == 0:
                    cnt += 1
                mp[i] += 1
                dq.append(i)
                result += len(dq)
        return result
    
    return tempFunc(s, k) - tempFunc(s, k - 1)