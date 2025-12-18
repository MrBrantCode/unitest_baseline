"""
QUESTION:
Given a string s containing 0's and 1's. You have to return the smallest positive integer C, such that the binary string can be cut into C pieces and each piece should be of the power of 5  with no leading zeros.
Note: The string s is a binary string. And if no such cuts are possible, then return -1.
Example 1:
Input:
s = "101101101"
Output: 
3
Explanation: 
We can split the given string into 
three 101s, where 101 is the binary 
representation of 5.
Example 2:
Input:
s = "00000"
Output: 
-1
Explanation: 
0 is not a power of 5.
Your Task:
Your task is to complete the function cuts() which take a single argument(string s). You need not take any input or print anything. Return an int C if the cut is possible else return -1.
Expected Time Complexity: O(|s|*|s|*|s|).
Expected Auxiliary Space: O(|s|).
Constraints:
1<= |s| <=50
"""

def find_min_cuts(s: str) -> int:
    def num(y: int) -> int:
        if y == 0:
            return 1
        x = 2
        for i in range(1, y):
            x = x << 1
        return x

    def check(n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 5 != 0:
            return False
        else:
            return check(n // 5)

    c = list(s)
    l = len(c)
    dp = [0] * (l + 1)
    dp[0] = 0
    
    for i in range(1, l + 1):
        index = i - 1
        if c[index] == '0':
            dp[i] = -1
        else:
            dp[i] = -1
            t = 1000
            count = 0
            for j in range(i):
                if c[index - j] == '1':
                    count += num(j)
                    if check(count) and dp[index - j] != -1:
                        w = 1 + dp[index - j]
                        t = min(w, t)
            if t != 1000:
                dp[i] = t
    
    return dp[l]