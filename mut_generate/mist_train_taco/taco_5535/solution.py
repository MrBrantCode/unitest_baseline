"""
QUESTION:
Xorgon is an extremely delicious treat formed by the sequence $S$ of binary integers $s_1, s_2,..,s_N$. A really interesting property found in a Xorgon is that the xor of all elements in any contiguous subsequence of length $K$ in $S$ will result in $1$.   
Chef has been asked to prepare a Xorgon. However, he has at his disposal a binary sequence $X$ containing the binary integers $x_1, x_2, ...x_N$. To prepare a Xorgon, the chef may flip the value of as many binary digits in $X$ as required.(i.e. turn a $1$ to a $0$ and $0$ to a $1$). Unfortunately, flipping a digit takes a lot of time and the chef has to serve many orders. Can you help the chef calculate the minimum number of flips required to cook a Xorgon from the given $X$?

-----Input:-----
- The first line will contain two space-separated integers $N, K$.
- Next line contains N space-separated integers $x_1, x_2, ...,x_N$. 

-----Output:-----
Output in a single line minimum number of flips required to turn $X$ into a Xorgon.

-----Constraints-----
- $1 \leq K \leq N \leq 3*10^6$
- $0 \leq x_i \leq 1$

-----Sample Input:-----
7 5
1 0 0 1 1 1 1

-----Sample Output:-----
1

-----EXPLANATION:-----
Flip the last bit from 1 to 0 to obtain a Xorgon.
"""

def min_flips_to_xorgon(n, k, arr):
    sol = []
    l = 0
    u = k
    while l != u:
        sol.append(arr[l:min(len(arr), u)])
        l = min(l + k, len(arr))
        u = min(u + k, len(arr))
    
    tiwari = []
    for i in range(k):
        titi = 0
        gao = 0
        for j in range(len(sol)):
            if len(sol[j]) > i:
                if sol[j][i] == 0:
                    titi += 1
                else:
                    gao += 1
        tiwari.append((titi, gao))
    
    minflip = (-1, -1)
    ans = 0
    ctr = 0
    for i in tiwari:
        if i[0] < i[1]:
            ans += i[0]
            ctr += 1
            if i[1] < minflip[0] or minflip[0] == -1:
                minflip = (i[1], i[0])
        else:
            ans += i[1]
            if i[0] < minflip[0] or minflip[0] == -1:
                minflip = (i[0], i[1])
    
    if ctr % 2 == 0:
        ans += minflip[0]
        ans -= minflip[1]
    
    return ans