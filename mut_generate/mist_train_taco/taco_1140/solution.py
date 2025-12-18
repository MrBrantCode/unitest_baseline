"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 

The problem is completely unrelated to its problem code :).

Let us build an infinite string D that is simply a concatenation of the decimal representations of all positive integers without leading zeros. In other words, D = 12345678910111213141...

You are given a string S. Find the position of the first occurrence of S in D that satisfies one additional constraint: at least one integer that was concatenated to form D occurs entirely within S.

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a string of digits S.

It is guaranteed that S will occur satisfying the given condition somewhere in D.

------ Output ------ 

For each test case, output a single line containing the minimal position number where S occurs in D under the given condition, modulo 10^{9}+7. Consider the string to be 1-indexed: '1' is in position 1.

------ Constraints ------ 

$1 ≤ T ≤ 10$
$1 ≤ |S| ≤ 300$
$Subtask 1 (17 points): the answer won't exceed 10^{7}$
$Subtask 2 (23 points): the answer will fit in a signed 64-bit integer (before taking modulo).$
$Subtask 3 (60 points): no additional constraints.$

------ Example ------ 

Input:
2
78910
9930

Output:
7
2679

------ Explanation ------ 

Please pay attention that in the second test case the answer is not 788, as it may seem at first glance. This is because the part 298299300301 doesn't contain any integer completely in it - neither 299, nor 300. But the part 928929930931932 contains the integer 930 completely.
"""

def find_position_in_infinite_string(S: str) -> int:
    def calc(w: int) -> int:
        w -= 1
        ans = 1
        t = 10
        d = 1
        while t - 1 <= w:
            ans += t // 10 * 9 * d
            d += 1
            t *= 10
        return ans + d * (w - t // 10 + 1)

    def solve(S: str) -> list:
        ans = []
        for K in range(1, len(S) + 1):
            if ans != []:
                break
            for N in range(K):
                sub = S[N:N + K]
                if sub[0] == '0':
                    continue
                v = w = int(sub)
                guess = sub
                if N > 0:
                    guess = (str(v - 1) + guess)[-N - K:]
                if guess != S[0:N + K]:
                    continue
                i = N + K
                good = True
                while good and len(guess) < len(S):
                    v += 1
                    guess = guess + str(v)
                    while good and i < len(S) and (i < len(guess)):
                        if S[i] != guess[i]:
                            good = False
                            break
                        i += 1
                if good:
                    ans.append(calc(w) - N)
        return ans

    ans = []
    ans.extend(solve(S))
    ans.append(calc(int('1' + S)) + 1)
    return min(ans) % 1000000007