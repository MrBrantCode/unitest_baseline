"""
QUESTION:
You are given an integer sequence of length N, a_1,a_2,...,a_N.

For each 1≤i≤N, you have three choices: add 1 to a_i, subtract 1 from a_i or do nothing.

After these operations, you select an integer X and count the number of i such that a_i=X.

Maximize this count by making optimal choices.

Constraints

* 1≤N≤10^5
* 0≤a_i<10^5 (1≤i≤N)
* a_i is an integer.

Input

The input is given from Standard Input in the following format:


N
a_1 a_2 .. a_N


Output

Print the maximum possible number of i such that a_i=X.

Examples

Input

7
3 1 4 1 5 9 2


Output

4


Input

10
0 1 2 3 4 5 6 7 8 9


Output

3


Input

1
99999


Output

1
"""

def maximize_equal_elements(sequence):
    cnt = {}
    
    def add(x):
        if x in cnt:
            cnt[x] += 1
        else:
            cnt[x] = 1
    
    for x in sequence:
        add(x - 1)
        add(x)
        add(x + 1)
    
    counts = map(lambda x: x[1], cnt.items())
    return max(counts)