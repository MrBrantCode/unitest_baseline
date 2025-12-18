"""
QUESTION:
Given a number S, you need to check whether any permutation of the number S divisible by 8 or not. 
Example 1:
Input: S = "80"
Output: "Divisible"
Explanation: 80 is divisible by 8
Example 2
Input: S = "101"
Output: "Not divisible"
Your Task :
Complete the function isDivisible8() that receives a string S denoting the number and returns 1 if any permutation of the number is divisible by 8 or else returns 0.
Expected Time Complexity : O(lS|^{3})
Expected Space Complexity : O(1)
Constraints:
1 ≤ lS| ≤ 10^{2}
"""

def is_divisible_by_8(S: str) -> str:
    if len(S) == 1:
        return "Divisible" if int(S) % 8 == 0 else "Not divisible"
    elif len(S) == 2:
        a = S[0]
        b = S[1]
        if int(a + b) % 8 == 0 or int(b + a) % 8 == 0:
            return "Divisible"
        return "Not divisible"
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            for k in range(j + 1, len(S)):
                a = S[i]
                b = S[j]
                c = S[k]
                if int(a + b + c) % 8 == 0:
                    return "Divisible"
    return "Not divisible"