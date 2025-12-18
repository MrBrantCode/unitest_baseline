"""
QUESTION:
The elections to Berland parliament are happening today. Voting is in full swing!

Totally there are n candidates, they are numbered from 1 to n. Based on election results k (1 ≤ k ≤ n) top candidates will take seats in the parliament.

After the end of the voting the number of votes for each candidate is calculated. In the resulting table the candidates are ordered by the number of votes. In case of tie (equal number of votes) they are ordered by the time of the last vote given. The candidate with ealier last vote stands higher in the resulting table.

So in the resulting table candidates are sorted by the number of votes (more votes stand for the higher place) and if two candidates have equal number of votes they are sorted by the time of last vote (earlier last vote stands for the higher place).

There is no way for a candidate with zero votes to take a seat in the parliament. So it is possible that less than k candidates will take a seat in the parliament.

In Berland there are m citizens who can vote. Each of them will vote for some candidate. Each citizen will give a vote to exactly one of n candidates. There is no option "against everyone" on the elections. It is not accepted to spoil bulletins or not to go to elections. So each of m citizens will vote for exactly one of n candidates.

At the moment a citizens have voted already (1 ≤ a ≤ m). This is an open election, so for each citizen it is known the candidate for which the citizen has voted. Formally, the j-th citizen voted for the candidate g_{j}. The citizens who already voted are numbered in chronological order; i.e. the (j + 1)-th citizen voted after the j-th.

The remaining m - a citizens will vote before the end of elections, each of them will vote for one of n candidates.

Your task is to determine for each of n candidates one of the three possible outcomes:

  a candidate will be elected to the parliament regardless of votes of the remaining m - a citizens;  a candidate has chance to be elected to the parliament after all n citizens have voted;  a candidate has no chances to be elected to the parliament regardless of votes of the remaining m - a citizens. 


-----Input-----

The first line contains four integers n, k, m and a (1 ≤ k ≤ n ≤ 100, 1 ≤ m ≤ 100, 1 ≤ a ≤ m) — the number of candidates, the number of seats in the parliament, the number of Berland citizens and the number of citizens who already have voted.

The second line contains a sequence of a integers g_1, g_2, ..., g_{a} (1 ≤ g_{j} ≤ n), where g_{j} is the candidate for which the j-th citizen has voted. Citizens who already voted are numbered in increasing order of voting times.


-----Output-----

Print the sequence consisting of n integers r_1, r_2, ..., r_{n} where:

  r_{i} = 1 means that the i-th candidate is guaranteed to take seat in the parliament regardless of votes of the remaining m - a citizens;  r_{i} = 2 means that the i-th candidate has a chance to take a seat in the parliament, i.e. the remaining m - a citizens can vote in such a way that the candidate will take a seat in the parliament;  r_{i} = 3 means that the i-th candidate will not take a seat in the parliament regardless of votes of the remaining m - a citizens. 


-----Examples-----
Input
3 1 5 4
1 2 1 3

Output
1 3 3 
Input
3 1 5 3
1 3 1

Output
2 3 2 
Input
3 2 5 3
1 3 1

Output
1 2 2
"""

class State:
    __slots__ = ['candidate', 'votes', 'last_vote']

    def __init__(self, cand, votes, last):
        self.candidate = cand
        self.votes = votes
        self.last_vote = last

    def beats(self, other, extra):
        return self.votes + extra > other.votes

def determine_candidate_outcomes(n, k, m, a, votes_cast):
    votes = [0 for _ in range(n)]
    last_vote = [0 for _ in range(n)]
    
    for t in range(a):
        cand = votes_cast[t] - 1
        votes[cand] += 1
        last_vote[cand] = t
    
    states = [State(i, votes[i], last_vote[i]) for i in range(n)]
    states = sorted(states, key=lambda x: (x.votes, -x.last_vote))
    
    res = [0 for _ in range(n)]
    
    for i in range(n):
        if i < n - k:
            low = n - k
            if states[i].beats(states[low], m - a):
                res[states[i].candidate] = 2
            else:
                res[states[i].candidate] = 3
        else:
            extra = m - a
            other = i - 1
            place = i
            if extra == 0 and states[i].votes == 0:
                res[states[i].candidate] = 3
                continue
            while other >= 0 and extra > 0:
                needed = states[i].votes - states[other].votes + 1
                if needed <= extra:
                    extra -= needed
                    place -= 1
                    other -= 1
                else:
                    break
            res[states[i].candidate] = 1 if place + k >= n and states[i].votes > 0 else 2
    
    return res