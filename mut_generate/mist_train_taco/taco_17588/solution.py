"""
QUESTION:
There are N piles of coins each containing  Ai (1<=i<=N) coins. Find the minimum number of coins to be removed such that the absolute difference of coins in any two piles is at most K.
Note: You can also remove a pile by removing all the coins of that pile.
Example 1:
Input:
N = 4, K = 0
arr[] = {2, 2, 2, 2}
Output:
0
Explanation:
For any two piles the difference in the
number of coins is <=0. So no need to
remove any coins. 
Example 2:
Input:
N = 6, K = 3
arr[] = {1, 5, 1, 2, 5, 1} 
Output :
2
Explanation:
If we remove one coin each from both
the piles containing 5 coins , then
for any two piles the absolute difference
in the number of coins is <=3. 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minSteps() which takes 2 integers N, and K and an array A of size N as input and returns the minimum number of coins that need to be removed.
Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
0 ≤ K ≤ 10^{4}
1 ≤ A[i] ≤ 103
"""

from collections import Counter

def min_steps_to_balance_piles(N, K, A):
    C = Counter(A)
    A = [[v, cnt] for (v, cnt) in C.items()]
    A.sort(key=lambda p: p[0])
    N = len(A)
    
    for i in range(N - 1, -1, -1):
        if A[i][0] - A[0][0] <= K:
            break
    i += 1
    
    if i >= N:
        return 0
    
    (allcnt, cost) = (0, 0)
    for j in range(i, N):
        allcnt += A[j][1]
        cost += (A[j][0] - A[0][0] - K) * A[j][1]
    
    ans = cost
    for j in range(N - 1):
        if A[N - 1][0] - A[j][0] <= K:
            break
        v = A[j][0]
        cost += v * A[j][1]
        vn = A[j + 1][0]
        diff = vn - v
        while i < N:
            if A[i][0] - vn <= K:
                cost -= (A[i][0] - v - K) * A[i][1]
                allcnt -= A[i][1]
                i += 1
            else:
                cost -= diff * allcnt
                break
        ans = min(ans, cost)
    
    return ans