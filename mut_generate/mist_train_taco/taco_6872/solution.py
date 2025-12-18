"""
QUESTION:
Consider a string with rings on both ends. Rings have positive integers to distinguish them. Rings on both ends of the string have different numbers a and b. Describe this as [a, b]. If there are multiple strings and the number attached to the ring of one string and the other string is the same, these strings can be connected at that ring, and the one made by connecting is called a chain. For example, the strings [1, 3] and [3, 4] form the chain [1, 3, 4]. The string and the chain or the chains are also connected at the ring with the same integer. Suppose you can.

For example, a chain [1, 3, 4] and a string [5, 1] ​​can form [5, 1, 3, 4], and a chain [1, 3, 4] and a chain [2, 3, 5] can form [5, 1, 3, 4]. The chain [1, 3, 4] and the chain [4, 6, 1] form a ring.

There are various shapes like this, but in some of them, rings with the same number follow only once. Multiple connected strings are called chains. For example, chains [1, 3, 4] The centrally crossed shape of the chains [2, 3, 5] also includes the chains [1, 3, 5], [2, 3, 4], and the chains [1, 3, 4]. And chains [4, 6, 1] loops include chains such as [1, 3, 4, 6], [3, 4, 6, 1], [4, 6, 1, 3]. ..

For these chains, the number contained is defined as the length. For a given number of strings, anything that can be connected can form a shape that contains one or more chains. Create a program to find the length of the chain.

The first line of the input data contains the number of strings, the positive integer 1 ≤ n ≤ 100, and each of the following n lines contains two integers a, b separated by blanks 1 ≤ a <b ≤ 100. The two integers in each line represent the integers at both ends of one string.

Input example 1 | Input example 2 | Input example 3
--- | --- | ---
|
7 | 6 | 7
1 3 | 1 2 | 1 3
3 4 | 2 3 | 2 4
1 4 | 3 4 | 3 5
2 7 | 4 5 | 4 6
5 7 | 1 5 | 6 7
6 7 | 2 6 | 2 6
1 7 | | 4 7
Output example 1 | Output example 2 | Output example 3
5 | 6 | 4

input

The input consists of multiple datasets. Input ends when n is 0. The number of datasets does not exceed 10.

output

For each dataset, the maximum chain length is output on one line.





Example

Input

7
1 3
3 4
1 4
2 7
5 7
6 7
1 7
6
1 2
2 3
3 4
4 5
1 5
2 6
7
1 3
2 4
3 5
4 6
6 7
2 6
4 7
0


Output

5
6
4
"""

def find_max_chain_length(n, rings):
    def dfs(ring, chain_len=1):
        unchecked[ring] = False
        unvisited[ring] = False
        len_rec[ring] = max(len_rec[ring], chain_len)
        for r in adj_list[ring]:
            if unvisited[r]:
                dfs(r, chain_len + 1)
        unvisited[ring] = True

    adj_list = [[] for _ in range(101)]
    for (a, b) in rings:
        adj_list[a].append(b)
        adj_list[b].append(a)

    len_rec = [1] * 101
    unchecked = [True] * 101
    unvisited = [True] * 101

    for r in set(sum(rings, ())):
        if unchecked[r]:
            dfs(r)

    dfs(len_rec.index(max(len_rec)))
    return max(len_rec)