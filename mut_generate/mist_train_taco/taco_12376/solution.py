"""
QUESTION:
Given a string S, check if it is possible to construct the given string S by performing any of the below operations any number of times. In each step, we can:
	Add any character at the end of the string.
	or, append the string to the string itself.
The above steps can be applied any number of times. The task is to find the minimum steps required to form the string.
Example 1:
Input: S = "aaaaaaaa"
Output: 4
Explanation: 
move 1: add 'a' to form "a"
move 2: add 'a' to form "aa"
move 3: append "aa" to form "aaaa"
move 4: append "aaaa" to form "aaaaaaaa"
Ã¢â¬â¹Example 2:
Input: S = "abcabca"
Output: 5
Explanation: 
move 1: add 'a' to form "a"
move 2: add 'b' to form "ab"
move 3: add 'c' to form "abc"
move 4: append "abc" to form "abcabc"
move 5: add 'a' to form "abcabca"
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minSteps() which takes the string s as inputs and returns the answer.
Expected Time Complexity: O(|S|^{2})
Expected Auxiliary Space: O(|S|)
Constraints:
1 ≤ |S| ≤ 10^{3}
"""

def min_steps_to_form_string(S: str) -> int:
    dp = [100000000] * len(S)
    dp[0] = 1
    for i in range(1, len(S)):
        if i % 2 == 1 and S[:i // 2 + 1] == S[i // 2 + 1:i + 1]:
            dp[i] = min(1 + dp[i // 2], dp[i])
        dp[i] = min(dp[i], dp[i - 1] + 1)
    return dp[len(S) - 1]