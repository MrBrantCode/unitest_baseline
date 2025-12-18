"""
QUESTION:
Given a string `senate` representing each senator's party belonging and an array `power` of integers representing each senator's power level, predict which party will finally announce the victory in a round-based voting procedure. The output should be `Radiant` or `Dire`. 

In the procedure, each senator can exercise one of two rights: ban one senator's right or announce the victory if all remaining senators are from the same party. A senator can only ban senators from the opposing party, and the power level of a senator determines the number of other senators they can ban in a single round. The length of the given string and the size of the power array will be in the range [1, 10,000], and the power level of each senator will be in the range [1, 100].
"""

import heapq

def predictPartyVictory(senate, power):
    n = len(senate)
    radiant = []
    dire = []
    for i in range(n):
        if senate[i] == 'R':
            heapq.heappush(radiant, (-power[i], i))
        else:
            heapq.heappush(dire, (-power[i], i))

    while radiant and dire:
        r_power, r_index = heapq.heappop(radiant)
        d_power, d_index = heapq.heappop(dire)
        if r_index < d_index:
            heapq.heappush(radiant, (r_power+1, r_index+n))  
        else:
            heapq.heappush(dire, (d_power+1, d_index+n))

    return 'Radiant' if radiant else 'Dire'