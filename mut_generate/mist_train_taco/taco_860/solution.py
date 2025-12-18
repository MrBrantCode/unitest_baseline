"""
QUESTION:
Bob just learned about bitwise operators. Since Alice is an expert, she decided to play a game, she will give a number $x$ to Bob and will ask some questions:
There will be 4 different kinds of queries:-
- 
Alice gives an integer $i$ and Bob has to report the status of the $i^{th}$ bit in $x$, the answer is $"ON"$ if it is on else $"OFF"$.
- 
Alice gives an integer $i$ and Bob has to turn on the $i^{th}$ bit in $x$.
- 
Alice gives an integer $i$ and Bob has to turn off the $i^{th}$ bit in $x$.
- 
Alice gives two integers $p$ and $q$ and in the binary representation of $x$ Bob has to swap the $p^{th}$ and the $q^{th}$ bits.
The value of $x$ changes after any update operation.
positions $i$, $p$, and $q$ are always counted from the right or from the least significant bit.
If anyone of $i$, $p$, or $q$ is greater than the number of bits in the binary representation of $x$, consider $0$ at that position.

-----Input:-----
- First-line will contain $T$, the number of test cases. Then the test cases follow. 
- the first line of each test case contains two space-separated integers $x, Q$.
- $2Q$ lines follow.
- first line is an integer, the query type.
- for each query of type 1 to 3, there will be the integer $i$
- for the query of type 4, there will be two space-separated integers, the integers $p, q$

-----Output:-----
For the queries of the first kind, print $"ON"$ or $"OFF"$.

-----Constraints-----
- $1 \leq T \leq 10^3$
- $1 \leq x \leq 10^9$
- $1 \leq Q \leq 10^3$
- $1 \leq i,p,q \leq 30$

-----Sample Input-----
1
2 2
2 
1
1 
1

-----Sample Output:-----
ON

-----EXPLANATION:-----
the binary representation of 2 is 10
for query 1, we just have to update x to 11 (or 3 in decimal).
for the next query, x is now 3 or 11 in binary so the answer is ON.
"""

def process_queries(x, queries):
    results = []
    for query in queries:
        if query[0] == 1:
            # Query Type 1: Check the status of the i-th bit
            i = query[1]
            if x & (1 << (i - 1)):
                results.append("ON")
            else:
                results.append("OFF")
        elif query[0] == 2:
            # Query Type 2: Turn on the i-th bit
            i = query[1]
            x |= (1 << (i - 1))
        elif query[0] == 3:
            # Query Type 3: Turn off the i-th bit
            i = query[1]
            x &= ~(1 << (i - 1))
        elif query[0] == 4:
            # Query Type 4: Swap the p-th and q-th bits
            p, q = query[1], query[2]
            bit_p = (x >> (p - 1)) & 1
            bit_q = (x >> (q - 1)) & 1
            if bit_p != bit_q:
                x ^= (1 << (p - 1))
                x ^= (1 << (q - 1))
    return results