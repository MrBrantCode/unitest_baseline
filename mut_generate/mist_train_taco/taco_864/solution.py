"""
QUESTION:
Demonstrative competitions will be held in the run-up to the 20NN Berlatov Olympic Games. Today is the day for the running competition!

Berlatov team consists of 2n runners which are placed on two running tracks; n runners are placed on each track. The runners are numbered from 1 to n on each track. The runner with number i runs through the entire track in i seconds.

The competition is held as follows: first runners on both tracks start running at the same time; when the slower of them arrives at the end of the track, second runners on both tracks start running, and everyone waits until the slower of them finishes running, and so on, until all n pairs run through the track.

The organizers want the run to be as long as possible, but if it lasts for more than k seconds, the crowd will get bored. As the coach of the team, you may choose any order in which the runners are arranged on each track (but you can't change the number of runners on each track or swap runners between different tracks).

You have to choose the order of runners on each track so that the duration of the competition is as long as possible, but does not exceed k seconds.

Formally, you want to find two permutations p and q (both consisting of n elements) such that sum = ∑_{i=1}^{n} max(p_i, q_i) is maximum possible, but does not exceed k. If there is no such pair, report about it.

Input

The first line contains two integers n and k (1 ≤ n ≤ 10^6, 1 ≤ k ≤ n^2) — the number of runners on each track and the maximum possible duration of the competition, respectively.

Output

If it is impossible to reorder the runners so that the duration of the competition does not exceed k seconds, print -1. 

Otherwise, print three lines. The first line should contain one integer sum — the maximum possible duration of the competition not exceeding k. The second line should contain a permutation of n integers p_1, p_2, ..., p_n (1 ≤ p_i ≤ n, all p_i should be pairwise distinct) — the numbers of runners on the first track in the order they participate in the competition. The third line should contain a permutation of n integers q_1, q_2, ..., q_n (1 ≤ q_i ≤ n, all q_i should be pairwise distinct) — the numbers of runners on the second track in the order they participate in the competition. The value of sum = ∑_{i=1}^{n} max(p_i, q_i) should be maximum possible, but should not exceed k. If there are multiple answers, print any of them.

Examples

Input


5 20


Output


20
1 2 3 4 5 
5 2 4 3 1 


Input


3 9


Output


8
1 2 3 
3 2 1 


Input


10 54


Output


-1

Note

In the first example the order of runners on the first track should be [5, 3, 2, 1, 4], and the order of runners on the second track should be [1, 4, 2, 5, 3]. Then the duration of the competition is max(5, 1) + max(3, 4) + max(2, 2) + max(1, 5) + max(4, 3) = 5 + 4 + 2 + 5 + 4 = 20, so it is equal to the maximum allowed duration.

In the first example the order of runners on the first track should be [2, 3, 1], and the order of runners on the second track should be [2, 1, 3]. Then the duration of the competition is 8, and it is the maximum possible duration for n = 3.
"""

def maximize_competition_duration(n, k):
    def tr(qq):
        return qq * (qq + 1) // 2

    if k < tr(n):
        return -1

    upp = 2 * (tr(n) - tr(n // 2))
    if n % 2 == 1:
        upp -= (n + 1) // 2

    if k >= upp:
        ans = list(range(1, n + 1))
        return upp, ans, ans[::-1]

    for kk in range(n // 2, n + 1):
        goal = k - tr(n) + tr(kk) - n
        lo = tr(kk - 1)
        hi = lo + (kk - 1) * (n - kk)
        if goal >= lo and goal <= hi:
            ex = goal - lo
            p = ex // (kk - 1)
            q = ex % (kk - 1)
            ansl = list(range(1 + p, kk + p))
            for i in range(q):
                ansl[kk - 2 - i] += 1
            ansls = set(ansl)
            ansr = []
            for i in range(1, n):
                if i not in ansls:
                    ansr.append(i)
            ans = ansl + [n] + ansr
            return k, list(range(1, n + 1)), ans

    return -1