"""
QUESTION:
At Akabe High School, a programmer training school, there is a unique study session run by the students themselves. It is important for programmers to constantly adopt new technologies, so the aim of this activity is to develop the habit of self-study through this study session.

There are a total of N students, each with a score obtained as a result of the programming contest at the time of admission. At the study session, some of the N students will become leaders, and each leader will run their own group and join the group they run.

Students other than the leader cannot join a group run by a leader with a score lower than their own. In addition, one value r that is 0 or more is decided so that the difference between the scores of the students participating in the group and the leader is within r. That is, if the leader of a group has a score of s and your score is greater than or less than s --r, you will not be able to join the group.

You are the executive committee chair of the study session and decided to do a simulation to prepare for the operation. In the simulation, start with no leader and repeat the following operations several times.

* Add students as leaders.
* Remove the student from the leader.
* For the combination of leaders at the time of request, find the minimum r such that the number of students who cannot participate in any group is x or less.



Create a program that performs such a simulation.



input

The input consists of one dataset. The input is given in the following format.


N Q
s1
s2
::
sN
QUERY1
QUERY2
::
QUERYQ


The first line gives the number of students N (1 ≤ N ≤ 1000000) and the number of processing requests Q (0 ≤ Q ≤ 1000).

The following N lines are given the integer si (0 ≤ si ≤ 1,000,000,000) indicating the score of the i-th student. Students shall be numbered 1,2, ..., N.

The processing request QUERYi is given to the following Q line. Processing requests are given in chronological order. There are three types of processing requests: ADD, REMOVE, and CHECK, and each QUERYi is given in one of the following formats.


ADD a


Or


REMOVE a


Or


CHECK x


ADD a stands for adding a student with the number a (1 ≤ a ≤ N) to the leader.

REMOVE a represents removing the student with the number a (1 ≤ a ≤ N) from the leader.

CHECK x represents an output request. An upper limit on the number of students who cannot join any group x (0 ≤ x ≤ N) is given.

The input shall satisfy the following conditions.

* At any given time, the number of leaders will not exceed 100.
* Do not add students who are leaders at that time to leaders.
* Students who are not leaders at that time will not be removed from the leader.

output

At the time of each output request in chronological order, the minimum r is output on one line so that the number of students who cannot join any group is x or less. However, if it is impossible to reduce the number of people to x or less no matter what r is selected, NA is output.

Example

Input

5 8
5
10
8
7
3
ADD 1
ADD 3
CHECK 0
CHECK 1
CHECK 2
CHECK 3
CHECK 4
CHECK 5


Output

NA
2
1
0
0
0
"""

from bisect import bisect
from collections import defaultdict

def simulate_study_session(N, Q, scores, queries):
    S = list(set(scores))
    S.sort()
    mp = {e: i for i, e in enumerate(S)}
    T = scores[:]
    T.sort()
    mpm = {e: i for i, e in enumerate(T)}
    INF = 10**9 + 1
    ps = []
    D = defaultdict(int)
    results = []

    for query in queries:
        t, x = query
        if t == 'ADD':
            y = scores[x - 1]
            if D[y] == 0:
                z = mp[y]
                idx = bisect(ps, z - 1)
                ps = ps[:idx] + [z] + ps[idx:]
            D[y] += 1
        elif t == 'REMOVE':
            y = scores[x - 1]
            D[y] -= 1
            if D[y] == 0:
                z = mp[y]
                idx = bisect(ps, z - 1)
                ps.pop(idx)
        elif t == 'CHECK':
            left = -1
            right = INF
            while left + 1 < right:
                mid = (left + right) >> 1
                prv = -1
                cnt = 0
                for e in ps:
                    s = S[e]
                    v = mpm[s]
                    idx = max(bisect(T, s - mid - 1) - 1, prv)
                    cnt += v - idx
                    prv = v
                if N - cnt <= x:
                    right = mid
                else:
                    left = mid
            if right == INF:
                results.append('NA')
            else:
                results.append(right)
    
    return results