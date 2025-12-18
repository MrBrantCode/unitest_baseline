"""
QUESTION:
Anuj has challenged Arun to climb N stairs but at only in powers of P and Q. Now Arun being a lazy guy wants to do this in minimum number of steps possible. So he has asked for your help to calculate the minimum number of steps he requires to take for climbing N stairs ( 1 step = some power of P or Q stairs (including zeroth power) ).
Example 1:
Input: 
N = 15, P = 2, Q = 3
Output:
3
Explanation:
We can make 15 by (8,4,3)
or (9,3,3) both takes 3 steps.
 
Example 2:
Input: 
N = 19, P = 4, Q = 3
Output:
2
Explanation:
In the second case, we can make
19 by (16,3) which is 2 steps.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function moves() which takes three integers N, P and Q as inputs and returns the number of steps that Arun needs to take to climb N stairs in powers of P & Q. If fit is not possible print -1.
 
Expected Time Complexity: O(N. log(N))
Expected Auxiliary Space: O(N. log(N))
 
Constraints:
1 ≤ N, P, Q ≤ 10^{5}
"""

from math import log

def minimum_steps_to_climb(N, P, Q):
    if P == 1 and Q == 1:
        return N
    if P == 1:
        P = Q
    if Q == 1:
        Q = P
    
    setti = set([N])
    count = 0
    
    while 0 not in setti:
        new = set()
        for item in setti:
            if item >= P ** int(log(item, P)):
                new.add(item - P ** int(log(item, P)))
            if item >= Q ** int(log(item, Q)):
                new.add(item - Q ** int(log(item, Q)))
        setti = new
        count += 1
    
    return count if 0 in setti else -1