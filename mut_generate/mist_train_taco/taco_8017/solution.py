"""
QUESTION:
Given N dice each with M faces, numbered from 1 to M, find the number of ways to get sum X. X is the summation of values on each face when all the dice are thrown.
 
Example 1:
Input:
M = 6, N = 3, X = 12
Output:
25
Explanation:
There are 25 total ways to get
the Sum 12 using 3 dices with
faces from 1 to 6.
Example 2:
Input:
M = 2, N = 3, X = 6
Output:
1
Explanation:
There is only 1 way to get
the Sum 6 using 3 dices with
faces from 1 to 2. All the
dices will have to land on 2.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function noOfWays() which takes 3 Integers M,N and X as input and returns the answer.
 
Expected Time Complexity: O(M*N*X)
Expected Auxiliary Space: O(N*X)
 
Constraints:
1 <= M,N,X <= 50
"""

def no_of_ways(M, N, X):
    curr = [0] * (X + 1)
    prev = [0] * (X + 1)
    prev[0] = 1
    
    for dice in range(1, N + 1):
        for target in range(1, X + 1):
            ans = 0
            for i in range(1, M + 1):
                if target - i >= 0:
                    ans += prev[target - i]
            curr[target] = ans
        prev = curr[:]
        curr = [0] * (X + 1)
    
    return prev[X]