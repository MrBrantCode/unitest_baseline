"""
QUESTION:
A new gangster is trying to take control of the city. He makes a list of his $N$ adversaries (e.g. gangster $\mbox{1}$, gangster $2$, ... gangster $N-1$, gangster $N$) and plans to get rid of them.

$\mbox{K}$ mercenaries are willing to do the job. The gangster can use any number of these mercenaries. But he has to honor one condition set by them: they have to be assigned in such a way that they eliminate a consecutive group of gangsters in the list, e.g. gangster $\boldsymbol{i}$, gangster $i+1$, ..., gangster $j-1$, gangster $j$, where the following is true: $1\leq i\leq j\leq N$.

While our new gangster wants to kill all of them, he also wants to pay the least amount of money. All mercenaries charge a different amount to kill different people. So he asks you to help him minimize his expenses.  

Input Format

The first line contains two space-separated integers, $N$  and $\mbox{K}$. Then $\mbox{K}$ lines follow, each containing $N$ integers as follows:

The $j^{th}$ number on the $i^{th}$ line is the amount charged by the $i^{th}$mercenary for killing the $j^{th}$ gangster on the list.

Constraints

$1\leq N\leq20$
$1\leq K\leq10$
$0\leq amount$ $charged\leq10000$

Output Format

Just one line, the minimum cost for killing the $N$ gangsters on the list.

Sample Input
3 2
1 4 1
2 2 2

Sample Output
 5

Explanation

The new gangster can assign mercenary 1 to kill gangster 1, and mercenary 2 to kill gangster 2 and gangster 3.
"""

def minimize_killing_cost(N, K, costs):
    def bits_free(x, K):
        res = []
        for i in range(K):
            if x % 2 == 0:
                res.append(i)
            x //= 2
        return res

    dpmat = [[[1000000 for _ in range(2 ** K)] for _ in range(K)] for _ in range(N)]
    
    for mer in range(K):
        dpmat[0][mer][1 << mer] = costs[mer][0]
    
    for gan in range(1, N):
        for lastmer in range(K):
            for mask in range(2 ** K):
                if dpmat[gan - 1][lastmer][mask] >= 1000000:
                    continue
                dpmat[gan][lastmer][mask] = min(dpmat[gan][lastmer][mask], dpmat[gan - 1][lastmer][mask] + costs[lastmer][gan])
                for newmer in bits_free(mask, K):
                    newmask = mask | 1 << newmer
                    dpmat[gan][newmer][newmask] = min(dpmat[gan][newmer][newmask], dpmat[gan - 1][lastmer][mask] + costs[newmer][gan])
    
    best = 1000000
    for lastmer in range(K):
        for mask in range(2 ** K):
            if dpmat[N - 1][lastmer][mask] < 0:
                continue
            best = min(best, dpmat[N - 1][lastmer][mask])
    
    return best