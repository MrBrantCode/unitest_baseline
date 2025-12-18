"""
QUESTION:
Shik loves sorted intervals. But currently he does not have enough time to sort all the numbers. So he decided to use Almost sorted intervals. An Almost sorted interval is a consecutive subsequence in a sequence which satisfies the following property:

The first number is the smallest.
The last number is the largest.

Please help him count the number of almost sorted intervals in this permutation.  

Note: Two intervals are different if at least one of the starting or ending indices are different.

Input Format 

The first line contains an integer N. 

The second line contains a permutation from 1 to N.

Output Format 

Output the number of almost sorted intervals.  

Constraints 

1 ≤ N ≤ $10^{6}  $

Sample Input  

5
3 1 2 5 4

Sample Output  

8

Explanation 

The subsequences [3], [1], [1 2], [1 2 5], [2], [2 5], [5], [4] are almost sorted intervals.
"""

import bisect

def count_almost_sorted_intervals(N, ais):
    intervals = []
    cur_interval = []
    cur_height = 0
    total_sequences = 0
    
    for i, ai in enumerate(ais):
        if ai < cur_height:
            merged = True
            while merged:
                if not intervals or intervals[-1][-1] > cur_interval[-1]:
                    intervals.append(cur_interval)
                    break
                pi = intervals.pop()
                mpi_top = bisect.bisect_right(pi, cur_interval[0])
                pi[mpi_top:] = cur_interval
                cur_interval = pi
            cur_interval = []
        cur_height = ai
        cur_interval.append(ai)
        total_sequences += len(cur_interval)
        prev_min = cur_interval[0]
        for prev_interval_i in range(len(intervals) - 1, -1, -1):
            pi = intervals[prev_interval_i]
            if pi[-1] > ai:
                break
            pi_lower = bisect.bisect_right(pi, prev_min)
            if pi_lower > 0:
                prev_min = pi[0]
            total_sequences += pi_lower
    
    return total_sequences