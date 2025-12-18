"""
QUESTION:
Given are integers N and X. For each integer k between 0 and X (inclusive), find the answer to the following question, then compute the sum of all those answers, modulo 998244353.

* Let us repeat the following operation on the integer k. Operation: if the integer is currently odd, subtract 1 from it and divide it by 2; otherwise, divide it by 2 and add 2^{N-1} to it. How many operations need to be performed until k returns to its original value? (The answer is considered to be 0 if k never returns to its original value.)

Constraints

* 1 \leq N \leq 2\times 10^5
* 0 \leq X < 2^N
* X is given in binary and has exactly N digits. (In case X has less than N digits, it is given with leading zeroes.)
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
X


Output

Print the sum of the answers to the questions for the integers between 0 and X (inclusive), modulo 998244353.

Examples

Input

3
111


Output

40


Input

6
110101


Output

616


Input

30
001110011011011101010111011100


Output

549320998
"""

def calculate_sum_of_operations(N: int, X: str) -> int:
    mod = 998244353
    rx = X.replace('1', '2').replace('0', '1').replace('2', '0')
    D = []
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            if N // i % 2:
                D += [i]
            if i != N // i and i % 2:
                D += [N // i]
    D.sort()
    cnt = [0] * len(D)
    ans = 0
    for k in range(len(D)):
        t = X[:D[k]]
        rt = rx[:D[k]]
        f = (t + rt) * (N // D[k] // 2) + t
        cnt[k] = cnt[k] + int(f <= X) + int(t, 2)
        cnt[k] %= mod
        ans += cnt[k] * D[k] * 2
        for kk in range(k + 1, len(D)):
            if D[kk] % D[k] == 0:
                cnt[kk] -= cnt[k]
                cnt[kk] %= mod
    return ans % mod