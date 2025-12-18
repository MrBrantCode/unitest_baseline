"""
QUESTION:
You are currently studying the language $A j o b$ ( which means strange in English ) from a renowned professor. The language has infinite number of letters in its alphabet ( now you know, why it is called ajob ).  

The professor taught you $N$ words, one by one. The number of letters in a word is equal to it's place in the teaching order. Thus, the $1^{st}$ word taught by the professor has $\mbox{1}$ letter, $2^{nd}$ word has $2$ letters, $3^{rd}$ word has $3$ letters, $\ldots$, the $N^{th}$ word has $N$ letters.  

All the letters within a word are distinct to each other.

Now, you are handed an assignment. You have to choose any one of the $N$ words and form a subsequence from it. The length of the subsequence should be exactly $\mbox{K}$ less than the length of original word. For example, if the length of the chosen word is $\mbox{L}$, then the length of the subsequence should be $L-K$. If for any word, $\mbox{L}$ is smaller than $\mbox{K}$ $\left(L<K\right)$, then you must not choose that word. Two subsequences are different to each other if, the lengths of them are different or they contain different characters in the same position.

Find the number of ways you can complete the assignment ${modulo}\:p$ ( ${p}$ will always be a $\textit{prime}$ ).  

1. 

The first line contains ${T}$, the number of testcases. The next ${T}$ lines contain three space separated integers $N$, ${K}$ and ${p}$.  

Output Format 

For each testcase, print one integer in a single line, the number possible ways you can complete the assignment, ${modulo}\:p$.

Constraints 

$1\leq T\leq100$ 

$2\leq N\leq10^{18}$ 

$0<K<N$ 

$2\leq p\leq10^5$ 

$p\:\text{is a Prime}$  

Sample Input #00  

3
2 1 2
2 1 5
5 3 13

Sample Output #00  

1
3
2

Sample Input #01  

5
5 2 3
6 5 11
7 6 3
6 5 7
6 5 5

Sample Output #01  

2
7
2
0
2
"""

def calculate_assignment_ways(n, k, p):
    memo = {}

    def C(n, k, p):
        fact = [1]
        for i in range(1, p):
            fact.append(fact[-1] * i % p)
        if p in memo:
            inv_fact = memo[p]
        else:
            inv = [0, 1]
            for i in range(2, p):
                inv.append(p - p // i * inv[p % i] % p)
            inv_fact = [1]
            for i in range(1, p):
                inv_fact.append(inv_fact[-1] * inv[i] % p)
            memo[p] = inv_fact
        ret = 1
        while n > 0:
            n1 = n % p
            k1 = k % p
            if k1 > n1:
                return 0
            ret = ret * fact[n1] * inv_fact[k1] * inv_fact[n1 - k1] % p
            n //= p
            k //= p
        return ret

    return C(n + 1, k + 1, p)