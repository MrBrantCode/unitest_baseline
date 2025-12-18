"""
QUESTION:
You are a king and you are at war. If the enemy breaks through your frontline you lose.
Enemy can break the line only if the sum of morale of any $K$ continuous soldiers is strictly less than $M$. So, you being a motivational orator decides to boost their morale by giving a speech. On hearing it morale of a soldier multiplies by $X$ which depends on you and your speech (i.e. $X$ can be any positive value) but atmost only $K$ continuous speakers can hear your speech.
N soldiers are standing on the frontline with $A[i]$ morale. 
Determine the minimum number of speeches you need to give.

-----Input:-----
The first line contains three space seperated integers $N,K,M$.
The next line contains $N$ space integers, ith of which denotes the morale of $ith$ soldier.

-----Output:-----
Output the minimum number of speeches required. In case if it is impossible to achieve, print $-1$.

-----Constraints:-----
$1 \leq N,M \leq 10^5$
$1 \leq k \leq N$
$0 \leq Ai \leq 10^5$ 

-----Sample Input:-----
6 2 5
1 1 1 1 1 1

-----Sample Output:-----
2

-----Explanation:-----
We multiply 2nd ,3rd  and 5th,6th by 5. Resulting array will be 1 5 5 1 5 5.
"""

def minimum_speeches_required(N, K, M, A):
    # Calculate the prefix sum array
    fsum = [A[0]]
    for i in range(1, N):
        fsum.append(fsum[i - 1] + A[i])
    
    # Initialize the count of speeches
    c = 0
    
    # First pass to check and boost morale
    i = K
    while i <= N:
        if i == K:
            s = fsum[i - 1]
        else:
            s = fsum[i - 1] - fsum[i - K - 1]
        
        if s == 0:
            c = -1
            break
        
        if s < M:
            c += 1
            if i < N:
                for j in range(i, i - K - 1, -1):
                    if A[j - 1] > 0:
                        j += K - 1
                        i = j
                        break
            if i < N:
                for j in range(i, i - K - 1, -1):
                    if A[j - 1] > 0:
                        j += K - 1
                        i = j
                        break
        i += 1
    
    # Second pass to ensure morale is sufficient
    i = K
    while i <= N:
        if i == K:
            s = fsum[i - 1]
        else:
            s = fsum[i - 1] - fsum[i - K - 1]
        
        if s == 0:
            c = -1
            break
        
        i += 1
    
    return c