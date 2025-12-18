"""
QUESTION:
Implement the `join_on_eq_with_dt` function that takes in two arrays `a1` and `a2` of equal length, two time arrays `t1` and `t2` of equal length, a time window `dt`, and a string `abs_rel` representing the type of time window ("abs_dt" or "rel_dt"). The function should perform a join operation based on equality with the specified time window and return two arrays `I` and `J` containing the indices of matching elements from `a1` and `a2` respectively. If no matches are found within the time window, the function should return empty arrays for `I` and `J`.
"""

import numpy as np

def join_on_eq_with_dt(a1, a2, t1, t2, dt, abs_rel):
    I = []
    J = []
    if abs_rel == "abs_dt":
        for i in range(len(a1)):
            for j in range(len(a2)):
                if a1[i] == a2[j] and abs(t1[i] - t2[j]) <= dt:
                    I.append(i)
                    J.append(j)
    elif abs_rel == "rel_dt":
        for i in range(len(a1)):
            for j in range(len(a2)):
                if a1[i] == a2[j] and abs(t1[i] - t2[j]) / max(abs(t1[i]), abs(t2[j])) <= dt:
                    I.append(i)
                    J.append(j)
    return np.array(I), np.array(J)