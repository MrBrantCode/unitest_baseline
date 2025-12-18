"""
QUESTION:
Gru wants to distribute $N$ bananas to $K$ minions on his birthday.
Gru does not like to just give everyone the same number of bananas, so instead, he wants to distribute bananas in such a way that each minion gets a $distinct$ amount of bananas. That is, no two minions should get the same number of bananas.
Gru also loves $gcd$. The higher the $gcd$, the happier Gru and the minions get. So help Gru in distributing the bananas in such a way that each Minion gets a distinct amount of bananas and gcd of this distribution is highest possible. Output this maximum gcd. If such a distribution is not possible output $-1$.
Note: You have to distribute $all$ $N$ bananas. 

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- Each testcase consists of a single line of input, which has two integers: $N, K$. 

-----Output:-----
For each testcase, output in a single line the maximum gcd or -1.

-----Constraints-----
- $1 \leq T \leq 100$
- $1 \leq N, K \leq 10^9$

-----Sample Input:-----
1
6 3

-----Sample Output:-----
1

-----EXPLANATION:-----
The only possible distribution is $[1, 2, 3]$. So the answer is 1.
"""

import math

def max_gcd_for_banana_distribution(N, K):
    # Calculate the sum of the first K natural numbers
    summ = K * (K + 1) // 2
    
    # Check if the distribution is possible
    if K > 44720 or summ > N:
        return -1
    
    # Find all factors of N
    factors = []
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            factors.append(i)
            if i != N // i:
                factors.append(N // i)
    
    # Sort factors in ascending order
    factors.sort()
    
    # Find the maximum gcd that is greater than or equal to summ
    for factor in factors:
        if factor >= summ:
            return N // factor
    
    return -1