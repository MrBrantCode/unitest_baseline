"""
QUESTION:
Given two integers N and M. Find the longest common contiguous subset in binary representation of both the numbers and print its decimal value.
Example 1:
Input: N = 10, M = 11
Output: 5
Explanation: 10 in Binary is "1010" and
11 in Binary is "1011". The longest common
contiguous subset is "101" which has a
decimal value of 5.
Ã¢â¬â¹Example 2:
Input: N = 8, M = 16
Output: 8
Explanation: 8 in Binary is "1000" and
16 in Binary is "10000". The longest common
contiguous subset is "1000" which has a
decimal value of 8.
Your Task:
You don't need to read input or print anything. Your task is to complete the function longestCommon() which takes two integers N and M as inputs and returns the Decimal representation of the longest common contiguous subset in the Binary representation of N and M.
Note: If there's a tie in the length of the longest common contiguous subset, return the one with the highest decimal value among them.
Expected Time Complexity: O((log(max (N, M))^{3}).
Expected Auxiliary Space: O((log(max (N, M))^{2}).
Constraints:
1<=N,M<=10^{18}
"""

def longest_common_contiguous_subset(N, M):
    # Convert N to binary and store its digits in reverse order
    d = []
    while N > 0:
        d.append(N % 2)
        N //= 2
    
    # Convert M to binary and store its digits in reverse order
    e = []
    while M > 0:
        e.append(M % 2)
        M //= 2
    
    # Dictionary to store all contiguous subsets of N's binary representation
    a1 = {}
    for i in range(len(d)):
        s = ''
        for j in range(i, len(d)):
            s += str(d[j])
            a1[s] = 1
    
    # Variable to store the result
    res = 0
    c2 = 0
    
    # Iterate over all contiguous subsets of M's binary representation
    for i in range(len(e)):
        s = ''
        c1 = 0
        c = 0
        p = 1
        for j in range(i, len(e)):
            c += p * e[j]
            p *= 2
            s += str(e[j])
            c1 += 1
            if s in a1:
                if c1 > c2:
                    res = c
                    c2 = c1
                elif c1 == c2:
                    res = max(res, c)
    
    return res