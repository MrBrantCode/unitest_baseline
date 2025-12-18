"""
QUESTION:
Babul’s favourite number is 17. He likes the numbers which are divisible by 17. This time what he does is that he takes a number n and tries to find the largest number which is divisible by 17, by rearranging the digits. As the number increases he gets puzzled with his own task. So you as a programmer have to help him to accomplish his task.
Note: If the number is not divisible by rearranging the digits, then return “Not Possible”. n may have leading zeros.
Example 1:
Input: n = 17
Output: 17
Explanation: 17 is the largest number 
which is also divisible by 17. 
Example 2:
Input: n = 15
Output: 51
Explanation: 51 is the largest number
which is also divisible by 17.
Your Task:  
You dont need to read input or print anything. Complete the function largestDivisible() which takes n as input parameter and returns the largest number which is divisible by 17.
Expected Time Complexity: O(|n|*|n|!), where |n| denoting length of n.
Expected Auxiliary Space: O(1)
Constraints:
1<= n <=10^{10}
"""

def find_largest_divisible_by_17(n: str) -> str:
    def solve(k, n, d):
        if k == n - 1:
            num = 0
            for i in d:
                num = num * 10 + i
            if num % 17 == 0 and num > ans[0]:
                ans[0] = num
            return
        solve(k + 1, n, d)
        for i in range(k + 1, n):
            if d[i] != d[i - 1]:
                (d[i], d[k]) = (d[k], d[i])
                solve(k + 1, n, d)
                (d[i], d[k]) = (d[k], d[i])

    digits = [ord(c) - ord('0') for c in n]
    ans = [-1]
    sz = len(n)
    solve(0, sz, digits)
    
    if ans[0] == -1:
        return 'Not Possible'
    return str(ans[0])