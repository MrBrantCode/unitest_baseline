"""
QUESTION:
-----Problem Statement-----
Chef studies combinatorics. He tries to group objects by their rang (a positive integer associated with each object). He also gives the formula for calculating the number of different objects with rang N as following:

the number of different objects with rang N = F(N) = A0 + A1 * N + A2 * N2 + A3 * N3.

Now Chef wants to know how many different multisets of these objects exist such that sum of rangs of the objects in the multiset equals to S. You are given the coefficients in F(N) and the target sum S. Please, find the number of different multisets modulo 1,000,000,007.

You should consider a multiset as an unordered sequence of integers. Two multisets are different if and only if there at least exists one element which occurs X times in the first multiset but Y times in the second one, where (X ≠ Y).

-----Input-----
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows. 

The first line of each test case contains four integers A0, A1, A2, A3. The second line contains an integer S.

-----Output-----
For each test case, output a single line containing a single integer - the answer to the test case modulo 1,000,000,007.

-----Constraints-----
- 1 ≤ T ≤ 500
- 1 ≤ S ≤ 100
- 0 ≤ Ai ≤ 1000
- Sum of all S for all test cases is not greater than 500. It's guaranteed that at least one Ai is non-zero.

-----Example-----
Input:
4
1 0 0 0
1
1 0 0 0
3
0 1 0 0
2
2 3 1 4
10

Output:
1
3
3
213986343

-----Explanation-----
Example case 2. 

In the second example function looks as follows F(N) = 1. So for each rang there is a single object of the rang. To get multiset with sum of rangs equal to 3, you can pick: three objects of rang 1, or one object of rang 1 and one of rang 2, or only one object of rang 3. 
Example case 3. 

In the third example function looks as follows F(N) = N. So, you have one distinct object of rang 1, two distinct objects of rang 2, three distinct objects of rang 3 and so on. To get
multiset with sum of rangs equal to 2, you can pick: two objects of rang 1, one of objects of rang 2 (two ways).
"""

def calculate_multisets(A0, A1, A2, A3, S):
    mod_val = 1000000007
    rang = [0] * 101
    pow_cache = [0] * 102
    multisets = {}

    def mod_pow(base, pow):
        result = 1
        while pow:
            if pow & 1:
                result = result * base % mod_val
            base = base * base % mod_val
            pow = pow >> 1
        return result

    def precalculate():
        for i in range(1, 102):
            pow_cache[i] = mod_pow(i, mod_val - 2)

    def cal_recurse(i, target_sum):
        if target_sum == 0:
            return 1
        if i >= target_sum:
            return 0
        if (i, target_sum) in multisets:
            return multisets[i, target_sum]
        ans = cal_recurse(i + 1, target_sum)
        max_pos = target_sum // (i + 1)
        choose = rang[i + 1] % mod_val
        for j in range(1, max_pos + 1):
            temp = choose * cal_recurse(i + 1, target_sum - j * (i + 1))
            ans += temp
            ans %= mod_val
            choose *= rang[i + 1] + j
            choose *= pow_cache[j + 1]
            choose %= mod_val
        multisets[i, target_sum] = ans
        return ans

    def populate(target_sum, rang_i):
        for i in range(1, target_sum + 1):
            rang[i] = rang_i[0] + (rang_i[1] + (rang_i[2] + rang_i[3] * i) * i) * i

    precalculate()
    populate(S, [A0, A1, A2, A3])
    return cal_recurse(0, S)