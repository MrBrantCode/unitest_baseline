"""
QUESTION:
Given are two sequences a=\{a_0,\ldots,a_{N-1}\} and b=\{b_0,\ldots,b_{N-1}\} of N non-negative integers each.
Snuke will choose an integer k such that 0 \leq k < N and an integer x not less than 0, to make a new sequence of length N, a'=\{a_0',\ldots,a_{N-1}'\}, as follows:
 - a_i'= a_{i+k \mod N}\ XOR \ x
Find all pairs (k,x) such that a' will be equal to b.What is \mbox{ XOR }?

The XOR of integers A and B, A \mbox{ XOR } B, is defined as follows:

 - When A \mbox{ XOR } B is written in base two, the digit in the 2^k's place (k \geq 0) is 1 if either A or B, but not both, has 1 in the 2^k's place, and 0 otherwise.
For example, 3 \mbox{ XOR } 5 = 6. (In base two: 011 \mbox{ XOR } 101 = 110.)


-----Constraints-----
 - 1 \leq N \leq 2 \times 10^5
 - 0 \leq a_i,b_i < 2^{30}
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N
a_0 a_1 ... a_{N-1}
b_0 b_1 ... b_{N-1}

-----Output-----
Print all pairs (k, x) such that a' and b will be equal, using one line for each pair, in ascending order of k (ascending order of x for pairs with the same k).
If there are no such pairs, the output should be empty.

-----Sample Input-----
3
0 2 1
1 2 3

-----Sample Output-----
1 3

If (k,x)=(1,3),
 - a_0'=(a_1\ XOR \ 3)=1
 - a_1'=(a_2\ XOR \ 3)=2
 - a_2'=(a_0\ XOR \ 3)=3
and we have a' = b.
"""

def find_matching_pairs(N, a, b):
    # Helper function to compute the prefix function for KMP algorithm
    def compute_prefix_function(s):
        w = [0] * N
        for i in range(1, N):
            j = w[i - 1]
            while j != 0 and s[i] != s[j]:
                j = w[j - 1]
            if s[i] == s[j]:
                w[i] = j + 1
            else:
                w[i] = 0
        return w

    # Compute the XOR differences for sequences a and b
    s = [a[i] ^ a[(i + 1) % N] for i in range(N)]
    t = [b[i] ^ b[(i + 1) % N] for i in range(N)] * 2

    # Compute the prefix function for s
    w = compute_prefix_function(s)

    # Find all valid k values using KMP algorithm
    k_list = []
    i, j = 0, 0
    while i < N:
        while j < N and t[i + j] == s[j]:
            j += 1
        if j == N:
            k_list.append(-i % N)
        if j == 0:
            i += 1
        else:
            i += j - w[j - 1]
            j = w[j - 1]

    # Sort k values
    k_list.sort()

    # Compute corresponding x values
    result = []
    for k in k_list:
        x = a[k] ^ b[0]
        result.append((k, x))

    return result