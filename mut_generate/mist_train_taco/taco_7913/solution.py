"""
QUESTION:
Given a boolean expression S of length N with following symbols.
Symbols
    'T' ---> true
    'F' ---> false
and following operators filled between symbols
Operators
    &   ---> boolean AND
    |   ---> boolean OR
    ^   ---> boolean XOR
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.
 
Example 1:
Input: N = 7
S = T|T&F^T
Output: 4
Explaination: The expression evaluates 
to true in 4 ways ((T|T)&(F^T)), 
(T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T)).
Example 2:
Input: N = 5
S = T^F|F
Output: 2
Explaination: ((T^F)|F) and (T^(F|F)) are the 
only ways.
 
Your Task:
You do not need to read input or print anything. Your task is to complete the function countWays() which takes N and S as input parameters and returns number of possible ways modulo 1003.
 
Expected Time Complexity: O(N^{3})
Expected Auxiliary Space: O(N^{2})
 
Constraints:
1 ≤ N ≤ 200
"""

def count_true_parenthesizations(N: int, S: str) -> int:
    mod = 1003
    dic = {}

    def solve(s: str, i: int, j: int, x: str) -> int:
        if i > j:
            return 0
        if i == j:
            if s[i] == x:
                return 1
            else:
                return 0
        temp = str(i) + ' ' + str(j) + ' ' + str(x)
        if temp in dic.keys():
            return dic[temp]
        k = i + 1
        ans = [0]
        while k < j:
            LT = solve(s, i, k - 1, 'T')
            LF = solve(s, i, k - 1, 'F')
            RT = solve(s, k + 1, j, 'T')
            RF = solve(s, k + 1, j, 'F')
            if s[k] == '&':
                if x == 'T':
                    ans[0] = (ans[0] + LT * RT % mod) % mod
                else:
                    ans[0] = (ans[0] + LT * RF % mod + LF * RT % mod + LF * RF % mod) % mod
            elif s[k] == '|':
                if x == 'T':
                    ans[0] = (ans[0] + LT * RT % mod + LT * RF % mod + LF * RT % mod) % mod
                else:
                    ans[0] = (ans[0] + LF * RF % mod) % mod
            elif s[k] == '^':
                if x == 'T':
                    ans[0] = (ans[0] + LT * RF % mod + LF * RT % mod) % mod
                else:
                    ans[0] = (ans[0] + LT * RT % mod + LF * RF % mod) % mod
            k += 2
        dic[temp] = ans[0] % mod
        return ans[0] % mod
    
    return solve(S, 0, N - 1, 'T')