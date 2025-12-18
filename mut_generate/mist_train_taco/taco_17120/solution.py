"""
QUESTION:
Every person likes prime numbers. Alice is a person, thus she also shares the love for them. Bob wanted to give her an affectionate gift but couldn't think of anything inventive. Hence, he will be giving her a graph. How original, Bob! Alice will surely be thrilled!

When building the graph, he needs four conditions to be satisfied:   It must be a simple undirected graph, i.e. without multiple (parallel) edges and self-loops.  The number of vertices must be exactly $n$ — a number he selected. This number is not necessarily prime.  The total number of edges must be prime.  The degree (i.e. the number of edges connected to the vertex) of each vertex must be prime. 

Below is an example for $n = 4$. The first graph (left one) is invalid as the degree of vertex $2$ (and $4$) equals to $1$, which is not prime. The second graph (middle one) is invalid as the total number of edges is $4$, which is not a prime number. The third graph (right one) is a valid answer for $n = 4$.  [Image] 

Note that the graph can be disconnected.

Please help Bob to find any such graph!


-----Input-----

The input consists of a single integer $n$ ($3 \leq n \leq 1\,000$) — the number of vertices.


-----Output-----

If there is no graph satisfying the conditions, print a single line containing the integer $-1$.

Otherwise, first print a line containing a prime number $m$ ($2 \leq m \leq \frac{n(n-1)}{2}$) — the number of edges in the graph. Then, print $m$ lines, the $i$-th of which containing two integers $u_i$, $v_i$ ($1 \leq u_i, v_i \leq n$) — meaning that there is an edge between vertices $u_i$ and $v_i$. The degree of each vertex must be prime. There must be no multiple (parallel) edges or self-loops.

If there are multiple solutions, you may print any of them.

Note that the graph can be disconnected.


-----Examples-----
Input
4

Output
5
1 2
1 3
2 3
2 4
3 4
Input
8

Output
13
1 2
1 3
2 3
1 4
2 4
1 5
2 5
1 6
2 6
1 7
1 8
5 8
7 8



-----Note-----

The first example was described in the statement.

In the second example, the degrees of vertices are $[7, 5, 2, 2, 3, 2, 2, 3]$. Each of these numbers is prime. Additionally, the number of edges, $13$, is also a prime number, hence both conditions are satisfied. [Image]
"""

def generate_prime_degree_graph(n):
    # List of prime numbers up to a reasonable limit
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097]
    
    if n in primes:
        m = n
        edges = [(i % n + 1, (i + 1) % n + 1) for i in range(n)]
        return m, edges
    
    ans = 0
    for prime in primes:
        if prime > n:
            ans = prime
            break
    
    if ans == 0:
        return -1
    
    m = ans
    x = (ans - n) * 2
    y = n - x
    index_start = 1
    index_mid = 2
    index_end = n
    flag = [0] * n
    edges = []
    
    for each_1 in range(n):
        if each_1 < x:
            sub = flag[index_start - 1]
            for each_2 in range(3 - sub):
                if index_start >= index_mid:
                    index_mid = index_start + 1
                edges.append((index_start, index_mid))
                flag[index_start - 1] += 1
                flag[index_mid - 1] += 1
                index_mid += 1
                if index_mid > index_end:
                    index_mid = index_start + 1
            index_start += 1
        else:
            sub = flag[index_start - 1]
            for each_2 in range(2 - sub):
                if index_start >= index_mid:
                    index_mid = index_start + 1
                edges.append((index_start, index_mid))
                flag[index_start - 1] += 1
                flag[index_mid - 1] += 1
                index_mid += 1
                if index_mid > index_end:
                    index_mid = index_start + 1
            index_start += 1
    
    return m, edges