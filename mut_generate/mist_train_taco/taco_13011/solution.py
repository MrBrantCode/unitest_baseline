"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 

Alok-nath is man of equality. He needs your help to divide his “sanskars” evenly amongst all his followers. By doing this, Alok-nath can create equality amongst his followers and he'll be called a true “sanskari”.

Alok-nath has N sanskars, and K followers. Each sanskar is given a numerical value which shows its intensity.

Your task is to determine whether it is possible to allocate all the sanskars to followers in such a way that the sum of intensities of the sanskars allocated to each follower is equal. Note : A sanskar can be allocated to only one of the followers.

------ Input ------ 

The first line of the input contains an integer T, denoting the number of test cases. Then T test cases follow. The first line of each case contains two integers N and K, with N denoting the number of sanskars and K denoting the number of followers. In the next line are N space separated integers denoting the intensities of each sanskar.

------ Output ------ 

For each test case, output "yes" if it is possible to divide his sanskars equally amongst his followers; otherwise output "no" (without quotes).

------ Constraints ------ 

$1 ≤ T ≤ 10$
$1 ≤ N ≤ 21$
$1 ≤ K ≤ 8$
$Subtask #1 (20 points) : 0 ≤ intensity of sanskar ≤ 10^{5}$
$Subtask #2 (80 points) : 0 ≤ intensity of sanskar ≤ 10^{10}$

----- Sample Input 1 ------ 
2
5 3
1 2 4 5 6
5 3
1 2 4 5 7
----- Sample Output 1 ------ 
yes
no
----- explanation 1 ------ 
In the first case, sanskars can be allocated as follows, each follower receiving a total intensity of 6: {1,5}, {2,4}, {6}.
"""

def can_divide_sanskars_equally(N, K, intensities):
    def outc(k, j, v, rs):
        if (k, j, tuple(v)) in book and rs == rs0:
            return book[k, j, tuple(v)]
        elif rs != 0 and j != n:
            res = False
            if not v[j]:
                if intensities[j] <= rs:
                    w = v.copy()
                    w[j] = True
                    res = res or outc(k, j + 1, w, rs - intensities[j])
            res = res or outc(k, j + 1, v, rs)
            book[k, j, tuple(v)] = res
            return res
        elif rs != 0 and j == n:
            return False
        elif rs == 0 and k != kk - 1:
            return outc(k + 1, 0, v, rs0)
        else:
            return True

    book = {}
    n, kk = N, K
    mysum = sum(intensities)
    
    if N < K or mysum % K != 0:
        return False
    
    rs0 = mysum // K
    return outc(0, 0, [False] * N, rs0)