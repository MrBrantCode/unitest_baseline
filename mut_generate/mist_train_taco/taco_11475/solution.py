"""
QUESTION:
Read problems statements in Mandarin chinese, Russian and Vietnamese as well. 

You are given a sequence A_{1}, A_{2}, ..., A_{N} and Q queries. In each query, you are given two parameters L and R; you have to find the smallest integer X such that 0 ≤ X < 2^{31} and the value of (A_{L} xor X) + (A_{L+1} xor X) + ... + (A_{R} xor X) is maximum possible.

Note: xor denotes the bitwise xor operation.

------ Input ------ 

The first line of the input contains two space-separated integers N and Q denoting the number of elements in A and the number of queries respectively.
The second line contains N space-separated integers A_{1}, A_{2}, ..., A_{N}.
Each of the next Q lines contains two space-separated integers L and R describing one query.

------ Output ------ 

For each query, print a single line containing one integer — the minimum value of X. 

------ Constraints ------ 

$1 ≤ N ≤ 10^{5}$
$1 ≤ Q ≤ 10^{5}$
$0 ≤ A_{i} < 2^{31} for each valid i$

------ Subtasks ------ 

Subtask #1 (18 points):

$1 ≤ N ≤ 10^{3}$
$1 ≤ Q ≤ 10^{3}$
$0 ≤ A_{i} < 2^{10} for each valid i$

Subtask #2 (82 points): original constraints

----- Sample Input 1 ------ 
5 3

20 11 18 2 13

1 3

3 5

2 4
----- Sample Output 1 ------ 
2147483629

2147483645

2147483645
"""

def find_optimal_x(A: list, queries: list) -> list:
    def count_bits(n: int) -> list:
        count = [0] * 62
        str2int = {'0': 0, '1': 31}
        for (i, b) in enumerate(f'{n:031b}'):
            count[i + str2int[b]] = 1
        return count

    def count_sum(c1: list, c2: list) -> list:
        return [i + j for (i, j) in zip(c1, c2)]

    def count_diff(c1: list, c2: list) -> list:
        return [i - j for (i, j) in zip(c1, c2)]

    def count2int(count: list) -> int:
        num = 0
        for i in range(31):
            if count[31 + i] < count[i]:
                num += 1 << 30 - i
        return num

    def get_counts(a: list) -> list:
        counts = [count_bits(a[0])]
        for i in range(1, len(a)):
            counts.append(count_sum(counts[i - 1], count_bits(a[i])))
        return counts

    def solve(counts: list, l: int, r: int) -> int:
        count = counts[r] if l == 0 else count_diff(counts[r], counts[l - 1])
        return count2int(count)

    results = []
    counts = get_counts(A)
    for (l, r) in queries:
        results.append(solve(counts, l - 1, r - 1))
    return results