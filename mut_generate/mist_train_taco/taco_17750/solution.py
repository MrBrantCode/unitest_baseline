"""
QUESTION:
You are given a binary string S of N bits. The bits in the string are indexed starting from 1. S[i] denotes the ith bit of S.

Let's say that a sequence i1, i2, …, iK(1 ≤ K; 1 ≤ i1 < i2 < … < iK ≤ N) produces a palindrome when applied to S, if the string S[i1] S[i2] … S[ik] is a palindrome (that is, reads the same backward or forward).

In addition, a sequence i1, i2, …, iK(1 ≤ K; 1 ≤ i1 < i2 < … < iK ≤ N) is said to be exponential, if ij + 1 = p * ij for each integer 1 ≤ j < K and for some integer p > 1. Note, that a sequence of one element is always exponential.

Your task is to count the number of exponential sequences that produce a palindrome when applied to S.

-----Input-----
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.

The only line of description for each test case contains a binary string S of N bits.

-----Output-----

For each test case, output a single line containing the number of exponential sequences that produce a palindrome.

-----Constraints-----
- 1 ≤ T ≤ 10
- Subtask 1(20 points): 1 ≤ N ≤ 20
- Subtask 2(30 points): 1 ≤ N ≤ 1000
- Subtask 3(50 points): 1 ≤ N ≤ 5 × 105

-----Note-----

The first test of the first subtask is the example test. It's made for you to make sure that your solution produces the same verdict both on your machine and our server.

-----Time Limits-----

Time limit for the first and the second subtasks is 3s. Time limit for the third subtask is 6s.

-----Example-----
Input:
2
11010
101001011

Output:
9
18

-----Explanation of the first case in the example test-----

The following sequences are counted in the answer: {1}, {2}, {3}, {4}, {5}, {1, 2}, {1, 4}, {2, 4}, {1, 2, 4}.
"""

def count_exponential_palindromes(S: str) -> int:
    def powerset(s):
        n = len(s)
        masks = [1 << j for j in range(n)]
        for i in range(2 ** n):
            yield [j + 1 for j in range(n) if masks[j] & i]

    def is_power2(num):
        return num != 0 and num & num - 1 == 0

    def special(l):
        n = len(l)
        for i in range(n):
            lis = [i + 1]
            yield lis
            for j in range(i + 1, n):
                p = l[j] / l[i]
                if p <= 1 or int(p) != p:
                    continue
                lis = [i + 1, j + 1]
                yield lis
                sk = (j + 1) * int(p)
                while sk <= n:
                    lis.append(sk)
                    sk *= int(p)
                    yield lis

    def expIndices(l):
        a = list(zip(l, l[1:]))
        if len(a) == 0:
            return True
        else:
            p = a[0][1] / a[0][0]
            if p <= 1 or int(p) != p:
                return False
            for i in range(1, len(a)):
                if a[i][1] / a[i][0] != p:
                    return False
            return True

    count = 0
    for i in special(range(1, len(S) + 1)):
        s = [S[j - 1] for j in i]
        if s == s[::-1]:
            count += 1
    return count