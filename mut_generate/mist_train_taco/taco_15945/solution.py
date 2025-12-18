"""
QUESTION:
Read problems statements in mandarin chinese, russian and vietnamese as well. 

	Fehc is Chef's best friend. They grew up with each other, and often help each other with competitive programming.

	Chef is participating in a programming contest prepared by Fehc and finds the following problem in Fehc's problem set: given a string s[1..N], count the number of pairs of indices 1 ≤ i ≤ j ≤ N such that s[i..j] is palindrome and j-i is even. The characters that may appear in s are 0, 1, 2, ..., 10^{9}.

	Chef doesn't know the solution, but he knows Fehc's habits of creating test data. When preparing data for a string problem, Fehc always generates a string of N 0's, and replaces some of the 0's by other characters. Thus, Chef assumes that there are only K nonzero characters in s, and K is usually much smaller than N.

	Given this useful information, can you help Chef solve this problem?
------ 
	Input ------ 

	The first line of input contains one integer T denoting the number of test cases.
	For each test case, the first line contains two space-separated integers N and K.
	K lines follow; the i-th of these lines contains two space-separated integers p_{i} and q_{i}, meaning that the i-th nonzero character is s[p_{i}] = q_{i}.

------ 
	Output ------ 

	For each test case, output one integer denoting the answer to the problem.

------ 
	Constraints ------ 

	$1 ≤ T ≤ 10$
	$1 ≤ N ≤ 10^{9}$
	$0 ≤ K ≤ 10^{5}$
	$1 ≤ p_{1} < p_{2} < ... < p_{K} ≤ N$
	$1 ≤ q_{i} ≤ 10^{9}$

	Subtask #1 (9 points):

	$N ≤ 1000$

	Subtask #2 (14 points):

	$N ≤ 10^{5}$

	Subtask #3 (21 points):

	$K ≤ 1000$

	Subtask #4 (56 points):

	$original constraints$

----- Sample Input 1 ------ 
3
7 2
5 1
6 1
7 3
2 1
4 2
6 1
10 0
----- Sample Output 1 ------ 
9
12
30
----- explanation 1 ------ 

	Example case 1: s={0,0,0,0,1,1,0}. The 9 pairs (i,j) are: (1,1), (2,2), ..., (7,7), (1,3) and (2,4).

	Example case 2: s={0,1,0,2,0,1,0}.

	Example case 3: s={0,0,0,0,0,0,0,0,0,0}.
"""

def count_even_length_palindromes(N, K, nonzero_positions):
    def getPLens(x):
        n = len(x)
        ret = [0] * n
        mx = 0
        mxi = 0
        for i in range(1, n):
            pp = min(ret[2 * mxi - i], mxi - i + ret[mxi])
            if pp < 0:
                pp = 0
            while True:
                a = i - pp
                b = i + pp
                if a < 0 or b >= n:
                    break
                if x[a] != x[b]:
                    break
                pp += 1
            pp -= 1
            ret[i] = pp
            if i + pp > mx:
                mx = i + pp
                mxi = i
        return ret

    def getBase(x):
        return x // 2 * (x // 2 + 1)

    def solve(x, n):
        p0 = 0
        ret = []
        for (a, b) in x:
            ret += [a - p0 - 1]
            ret += [b]
            p0 = a
        ret += [n - p0]
        pp = getPLens(ret)
        cmlen = [0]
        for (i, z) in enumerate(ret):
            if i % 2 == 0:
                cmlen += [cmlen[-1] + z]
            else:
                cmlen += [cmlen[-1] + 1]
        rr = 0
        for (i, p) in enumerate(pp):
            if i % 2 == 0:
                rr += getBase(ret[i])
            if i % 2 == 0 and ret[i] % 2 == 0:
                continue
            i0 = i - p
            i1 = i + p
            ll = cmlen[i1 + 1] - cmlen[i0]
            if i0 % 2 == 1:
                ll += min(ret[i0 - 1], ret[i1 + 1]) * 2
            rr += (ll + 1) // 2
        return rr

    return solve(nonzero_positions, N)