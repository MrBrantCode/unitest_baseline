"""
QUESTION:
There are N strings arranged in a row. It is known that, for any two adjacent strings, the string to the left is lexicographically smaller than the string to the right. That is, S_1<S_2<...<S_N holds lexicographically, where S_i is the i-th string from the left.

At least how many different characters are contained in S_1,S_2,...,S_N, if the length of S_i is known to be A_i?

Constraints

* 1 \leq N \leq 2\times 10^5
* 1 \leq A_i \leq 10^9
* A_i is an integer.

Input

Input is given from Standard Input in the following format:


N
A_1 A_2 ... A_N


Output

Print the minimum possible number of different characters contained in the strings.

Examples

Input

3
3 2 1


Output

2


Input

5
2 3 2 1 2


Output

2
"""

def minimum_different_characters(N, A):
    def check(K):
        stack = []
        n = A[0]
        for i in range(1, N):
            if A[i - 1] < A[i]:
                n = A[i]
            else:
                if K == 1:
                    return False
                n = A[i]
                while True:
                    l = 0
                    if stack:
                        l = stack[-1][0]
                    if l > n:
                        stack.pop()
                    else:
                        break
                k = n
                while k >= 1:
                    if not stack:
                        stack.append([k, 1])
                        break
                    if stack[-1][0] == k:
                        if stack[-1][1] == K - 1:
                            if k != 1:
                                stack.pop()
                                k -= 1
                            else:
                                return False
                        else:
                            stack[-1][1] += 1
                            break
                    else:
                        stack.append([k, 1])
                        break
        return True

    (l, r) = (1, N)
    while l < r:
        m = (l + r) // 2
        if check(m):
            r = m
        else:
            l = m + 1
    return l