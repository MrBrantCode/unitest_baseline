"""
QUESTION:
Master Shifu is training Po to become The Dragon Warrior and as a final assignment he must obtain maximum deliciousness from dumplings. There are  $N$ plates of dumplings in front of him with deliciousness $A_1, A_2, \ldots, A_N$, Po can choose any number of continuous plates of  dumplings. The total deliciousness is the sum of deliciousness of all the  chosen dumplings.
What is the minimum number of plates he must choose so that total deliciousness is maximum possible?
Note: Po must choose atleast one plate.

-----Input:-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

-----Output:-----
For each test case, print a single line containing one integer.

-----Constraints-----
- $1 \le T \le 10$
- $1 \le N \le 2 \cdot 10^5$
- $0 \le A_i \le 10^9$

-----Sample Input:-----
2
4
1 2 3 4
5
3 2 0 3 0

-----Sample Output:-----
4
4
"""

def max_deliciousness_plates(test_cases):
    results = []
    
    for case in test_cases:
        N, A = case
        count = 0
        last = 0
        
        # Count leading zeros
        for i in range(N):
            if A[i] != 0:
                break
            last = i
            count += 1
        
        # Count trailing zeros
        for i in A[-1:last:-1]:
            if i != 0:
                break
            count += 1
        
        # Calculate the minimum number of plates to choose
        ans = N - count
        if ans == 0:
            results.append(1)
        else:
            results.append(ans)
    
    return results