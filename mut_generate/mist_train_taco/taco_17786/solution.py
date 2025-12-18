"""
QUESTION:
Given a positive integer X. The task is to find the smallest even number E such that
E > X and all digits in X and E are the same.
Note: All the digits in X should be same with digits in E.
 
Example 1:
Input:
X = 34722641
Output:
34724126
Explanation:
Next greater number with same 
digits as in input is 34724126.
Example 2:
Input:
X = 111
Output:
-1
Explanation:
You can't rearrange the digits to get an answer.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function getNextEven() which takes a string X as input, which is representing the number and returns the required smallest even number. If no such even number exists return -1.
Expected Time Complexity: O(Log(N)! )
Expected Auxiliary Space: O(Log(N))
Constraints:
1 ≤ N ≤ 10^{9}
"""

def get_next_even(x: str) -> int:
    s, p, flag, r = [], 0, 0, int(x)
    
    # Check if there is any even digit in the number
    for i in x:
        p += int(i)
        if int(i) % 2 == 0:
            flag = 1
        s.append(i)
    
    # If no even digit, return -1
    if flag == 0:
        return -1
    
    n, x = len(s), int(x)
    
    # Find the next greater number with the same digits
    while r % 2 != 0 or r <= x:
        l, k = -1, -1
        for i in range(n - 2, -1, -1):
            if s[i] < s[i + 1]:
                k = i
                break
        if k == -1:
            return -1
        for i in range(k + 1, n):
            if s[k] < s[i]:
                l = i
        s[k], s[l] = s[l], s[k]
        s = s[:k + 1] + s[k + 1:][::-1]
        r = int(''.join(s))
    
    return r