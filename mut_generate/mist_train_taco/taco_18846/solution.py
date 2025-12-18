"""
QUESTION:
Given a string S that contains only digits (0-9) and an integer target, return all possible strings to insert the binary operator ' + ', ' - ', or ' * ' between the digits of S so that the resultant expression evaluates to the target value.
Note:
 Operands in the returned expressions should not contain leading zeros. For example, 2 + 03 is not allowed whereas 20 + 3 is fine. It is allowed to not insert any of the operators.
If no solution is found, return an empty string array.
Example 1:
Input:
S = "123"
target = 6
Output: { "1*2*3", "1+2+3"}
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
Example 2:
Input:
S = "3456237490"
target = 9191
Output: { } 
Explanation: There are no expressions that can be created from "3456237490"  to evaluate to 9191.
Example 3:
Input:
S = "12"
target = 12
Output: { "12"} 
Explanation: S itself matches the target. No other strings are possible.
Your Task:
You don't need to read input or print anything. Your task is to complete the function addOperators() which takes string S and integer target as parameters and returns a list of strings that contains all valid possibilities.
Expected Time Complexity: O(|S|*4^{|}^{S|})
Expected Auxiliary Space: O(|s|*3^{|S|})
Constraints:
1 ≤ |S| ≤ 10
S consists of only digits.
-2^{31 }≤ target ≤ 2^{31}-1
"""

def find_expressions(S: str, target: int) -> list[str]:
    def solve(ind, S, target, evalu, ans, res, mul):
        if ind == len(S):
            if evalu == target:
                res.append(ans)
            return
        for i in range(ind, len(S)):
            if ind != i and S[ind] == '0':
                break
            cur = int(S[ind:i + 1])
            if ind == 0:
                solve(i + 1, S, target, cur, ans + str(cur), res, cur)
            else:
                solve(i + 1, S, target, evalu + cur, ans + '+' + str(cur), res, cur)
                solve(i + 1, S, target, evalu - cur, ans + '-' + str(cur), res, -cur)
                solve(i + 1, S, target, evalu - mul + mul * cur, ans + '*' + str(cur), res, mul * cur)

    if int(S) == target:
        return [S]
    ans = ''
    res = []
    solve(0, S, target, 0, ans, res, 0)
    return res