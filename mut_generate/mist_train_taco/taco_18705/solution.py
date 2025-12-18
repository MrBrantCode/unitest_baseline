"""
QUESTION:
Geek is very fond of chocolates. But he can't reach the kitchen shelf which has 'N' chocolates. His family has K members and he can call any number of family members to help him out. After acquiring the chocolates, the family members that Geek called will first divide the chocolates amongst themsleves equally. They do this in such a way that they all get maximum number of chocolates. The remaining chocolates are given to Geek. 
Find the maximum number of chocolates that Geek can get.
Example 1:
Input: 
N = 15, K = 4
Output: 3
Explaination: 
Calling 1 member. Geek will get nothing. 
Calling 2 members. Geek will get 1 chocolate. 
Calling 3 members. Geek will get nothing. 
Calling 4 members. Geek will get 3 chocolates. 
Example 2:
Input: 
N = 19, K = 5
Output: 4
Explaination: 5 memebers will be called who will 
divide 15 chocolates among them. And 4 chocolates 
will be left for Geek. 
Your Task:
You do not need to read input or print anything. Your task is to complete the function maxChocolate() which takes N and K as input parameters and returns the maximum number of chocolates Geek can have.
Expected Time Complexity: O(min(N,K))
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N, K ≤ 10^{5}
"""

def max_chocolates(N: int, K: int) -> int:
    if K > N:
        return N
    else:
        r = 0
        for i in range(1, K + 1):
            r = max(r, N % i)
    return r