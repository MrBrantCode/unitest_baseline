"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

Chef is playing a new computer game in which he is the chef of a restaurant and is required to prepare the dishes ordered by the customers with high quality and in time.

Chef will start in level 1 and whenever Chef passes a level in this game he will advance to the next level, but if Chef fails, he will return to level 1.

Chef has already played N rounds, but he can't remember what the levels were in all the rounds. He will give you an array A of length N such that A_{i} is equal to -1 if Chef can't remember what level the i-th round was, otherwise it will contain positive integer denoting the level of the round.

Now Chef is asking you to count the number of ways to fill the missing numbers (ie. the -1s) of the array with level numbers, so that it corresponds to a valid game. Since the answer can be large, output it modulo 10^{9}+7.

------ Input ------ 

First line contains an integer T, the number of test-cases.

First line of each test-case contains an integer N.

Second line contains N space-separated integers, which are the elements of the array A.

------ Output ------ 

Output the answer for each test-case in new line, the number of ways modulo  10^{9}+7.

------ Constraints ------ 

$1 ≤ T ≤ 10,000$
$1 ≤ N ≤ 100,000$
$sum of N in all test-cases will not exceed 100,000$
$1 ≤ A_{i} ≤ N or A_{i} = -1$

----- Sample Input 1 ------ 
1
6
1 1 2 -1 -1 2
----- Sample Output 1 ------ 
2
----- explanation 1 ------ 
The only two valid fully filled arrays are (1,1,2,3,1,2) and (1,1,2,1,1,2). Hence the answer is 2.
"""

MOD = 10 ** 9 + 7

def count_valid_game_ways(N, A):
    def solve():
        for i in range(N - 1, 0, -1):
            if A[i] != -1 and A[i] != 1:
                peeche_must_be = A[i] - 1
                peeche = A[i - 1]
                if peeche == -1:
                    A[i - 1] = peeche_must_be
                elif peeche != peeche_must_be:
                    return 0
        if A[0] != -1 and A[0] != 1:
            return 0
        ans = 1
        k = 0
        for i in range(1, N):
            if A[i] == -1:
                k += 1
        return pow(2, k, MOD)
    
    return solve()