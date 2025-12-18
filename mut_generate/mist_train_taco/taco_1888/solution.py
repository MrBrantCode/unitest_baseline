"""
QUESTION:
There are n students at Berland State University. Every student has two skills, each measured as a number: a_{i} — the programming skill and b_{i} — the sports skill.

It is announced that an Olympiad in programming and sports will be held soon. That's why Berland State University should choose two teams: one to take part in the programming track and one to take part in the sports track.

There should be exactly p students in the programming team and exactly s students in the sports team. A student can't be a member of both teams.

The university management considers that the strength of the university on the Olympiad is equal to the sum of two values: the programming team strength and the sports team strength. The strength of a team is the sum of skills of its members in the corresponding area, so the strength of the programming team is the sum of all a_{i} and the strength of the sports team is the sum of all b_{i} over corresponding team members.

Help Berland State University to compose two teams to maximize the total strength of the university on the Olympiad.


-----Input-----

The first line contains three positive integer numbers n, p and s (2 ≤ n ≤ 3000, p + s ≤ n) — the number of students, the size of the programming team and the size of the sports team.

The second line contains n positive integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 3000), where a_{i} is the programming skill of the i-th student.

The third line contains n positive integers b_1, b_2, ..., b_{n} (1 ≤ b_{i} ≤ 3000), where b_{i} is the sports skill of the i-th student.


-----Output-----

In the first line, print the the maximum strength of the university on the Olympiad. In the second line, print p numbers — the members of the programming team. In the third line, print s numbers — the members of the sports team.

The students are numbered from 1 to n as they are given in the input. All numbers printed in the second and in the third lines should be distinct and can be printed in arbitrary order.

If there are multiple solutions, print any of them.


-----Examples-----
Input
5 2 2
1 3 4 5 2
5 3 2 1 4

Output
18
3 4 
1 5 

Input
4 2 2
10 8 8 3
10 7 9 4

Output
31
1 2 
3 4 

Input
5 3 1
5 2 5 1 7
6 3 1 6 3

Output
23
1 3 5 
4
"""

from itertools import accumulate
from heapq import heappop, heappush

def maximize_university_strength(n, p, s, a, b):
    def top(ppl_indices, vals, start):
        Q = []
        res = [0 for i in range(len(ppl_indices))]
        for k, idx in enumerate(ppl_indices):
            heappush(Q, -vals[idx])
            if k >= start:
                res[k] = res[k - 1] - heappop(Q)
        return res

    conversion_gain = [y - x for x, y in zip(a, b)]
    ordered_by_a = sorted(zip(a, range(n)), reverse=True)
    prefix_sums_a = list(accumulate([x for x, y in ordered_by_a]))
    conversions = top([idx for val, idx in ordered_by_a], conversion_gain, p)
    rest_of_bs = list(reversed(top([idx for val, idx in reversed(ordered_by_a[p:])], b, n - p - s))) + [0]
    
    sol, top_k = max([(prefix_a + convert + add_bs, idx) 
                      for idx, (prefix_a, convert, add_bs) 
                      in enumerate(zip(prefix_sums_a[p - 1:p + s], 
                                       conversions[p - 1:p + s], 
                                       rest_of_bs))])
    
    top_k += p
    conversion_ordered_by_a = [(conversion_gain[idx], idx) for val, idx in ordered_by_a]
    conversion_sorted = sorted(conversion_ordered_by_a[:top_k], reverse=True)
    converted = [idx for val, idx in conversion_sorted[:top_k - p]]
    team_a = list(set((idx for val, idx in ordered_by_a[:top_k])) - set(converted))
    b_ordered_by_a = [(b[idx], idx) for val, idx in ordered_by_a]
    b_sorted = sorted(b_ordered_by_a[top_k:], reverse=True)
    team_b = converted + [idx for val, idx in b_sorted[:p + s - top_k]]
    
    return sol, [idx + 1 for idx in team_a], [idx + 1 for idx in team_b]