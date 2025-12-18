"""
QUESTION:
Berland shop sells $n$ kinds of juices. Each juice has its price $c_i$. Each juice includes some set of vitamins in it. There are three types of vitamins: vitamin "A", vitamin "B" and vitamin "C". Each juice can contain one, two or all three types of vitamins in it.

Petya knows that he needs all three types of vitamins to stay healthy. What is the minimum total price of juices that Petya has to buy to obtain all three vitamins? Petya obtains some vitamin if he buys at least one juice containing it and drinks it.


-----Input-----

The first line contains a single integer $n$ $(1 \le n \le 1\,000)$ — the number of juices.

Each of the next $n$ lines contains an integer $c_i$ $(1 \le c_i \le 100\,000)$ and a string $s_i$ — the price of the $i$-th juice and the vitamins it contains. String $s_i$ contains from $1$ to $3$ characters, and the only possible characters are "A", "B" and "C". It is guaranteed that each letter appears no more than once in each string $s_i$. The order of letters in strings $s_i$ is arbitrary.


-----Output-----

Print -1 if there is no way to obtain all three vitamins. Otherwise print the minimum total price of juices that Petya has to buy to obtain all three vitamins.


-----Examples-----
Input
4
5 C
6 B
16 BAC
4 A

Output
15

Input
2
10 AB
15 BA

Output
-1

Input
5
10 A
9 BC
11 CA
4 A
5 B

Output
13

Input
6
100 A
355 BCA
150 BC
160 AC
180 B
190 CA

Output
250

Input
2
5 BA
11 CB

Output
16



-----Note-----

In the first example Petya buys the first, the second and the fourth juice. He spends $5 + 6 + 4 = 15$ and obtains all three vitamins. He can also buy just the third juice and obtain three vitamins, but its cost is $16$, which isn't optimal.

In the second example Petya can't obtain all three vitamins, as no juice contains vitamin "C".
"""

def minimum_juice_cost(n, juices):
    # Initialize a large number for comparison
    INF = 1000000
    
    # Initialize the options array with a large number
    opts = [INF] * 8
    opts[0] = 0
    
    # Process each juice
    for price, vitamins in juices:
        v = 0
        if 'A' in vitamins:
            v += 1
        if 'B' in vitamins:
            v += 2
        if 'C' in vitamins:
            v += 4
        opts[v] = min(opts[v], price)
    
    # Helper function to calculate minimum cost
    def minv(a, b=0, c=0):
        if a | b | c != 7:
            return INF
        return opts[a] + opts[b] + opts[c]
    
    # Calculate the minimum cost to get all vitamins
    mins = INF
    for a in range(1, 8):
        mins = min(mins, minv(a))
        for b in range(a + 1, 8):
            mins = min(mins, minv(a, b))
            for c in range(b + 1, 8):
                mins = min(mins, minv(a, b, c))
    
    # Return the result
    return -1 if mins >= INF else mins