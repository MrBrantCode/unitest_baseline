"""
QUESTION:
The integers $0$ to $M - 1$ have been arranged in a circular fashion. That is, $0, 1, 2, \ldots, M - 1$, are in that order and
also, $0$ and $M - 1$ are next to each other. The distance between any two adjacent numbers on this circle is 1. You are given $N$ intervals on this, such that no two intervals touch or intersect with each other. The i-th interval will be of the form [$L_{i}, R_{i}$]. This means that the i-th interval contains all the integers between $L_{i}$ and $R_{i}$, both end points inclusive. You are supposed to mark exactly one number inside each interval, in such a way that the minimum distance between any two marked numbers is maximized.

More formally, we have $0 ≤ L_{1} ≤ R_{1} < L_{2} ≤ R_{2} < L_{3} \ldots < L_{N} ≤ R_{N} ≤ M - 1$. You are supposed to mark exactly $N$ numbers: $A_{1}, A_{2}, \ldots, A_{N}$, such that $L_{i} ≤ A_{i} ≤ R_{i}$ for all $1 ≤ i ≤ N$. And you want to do it in such a manner $min_{i \neq j}$ (shortest distance between $A_{i}$ and $A_{j}$ ), is maximized.

------ Input: ------

First line of the input contains a pair of integers $M$ and $N$.
The i-th of the next $N$ lines contains two numbers $L_{i}$ and $R_{i}$ which denote the end points of the i-th interval.

------ Output: ------
A single integer denoting the maximized minimum distance between any two marked numbers.

------ Constraints  ------
$1 ≤ M ≤ 10^{18}$
$2 ≤ N ≤ 4 * 10^{5}$

------ Subtasks ------
10 points : 
	- $1 ≤ M ≤ 10000$
	- $2 ≤ N ≤ 100$
25 points : 
	- $1 ≤ M ≤ 10^{18}$
	- $2 ≤ N ≤ 1000$
65 points : No further constraints.

----- Sample Input 1 ------ 
9 3
0 2
3 4
5 7
----- Sample Output 1 ------ 
3
----- explanation 1 ------ 
We can choose $A_{1} = 0, A_{2} = 3, A_{3} = 6$. The distance between every adjacent marked pair of numbers is 3, and hence that is the minimum. You can check that you cannot do any better, and hence 3 is the answer.
"""

def maximize_min_distance(m, n, intervals):
    def possible_with_dist(intervals, dist):
        first = prev_placed = intervals[0][0] - dist
        if not (first >= intervals[0][0] and first <= intervals[0][1]):
            if first > intervals[0][1]:
                first = prev_placed = intervals[0][1]
            else:
                first = prev_placed = intervals[0][0]
        for i in range(1, len(intervals)):
            next_pos = prev_placed + dist
            if next_pos < intervals[i][0]:
                prev_placed = intervals[i][0]
            elif not next_pos <= intervals[i][1]:
                return False
            else:
                prev_placed = next_pos
        if first + m - prev_placed < dist:
            return False
        return True

    def upper_bound(intervals):
        lo, hi = 1, m
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if possible_with_dist(intervals, mid):
                lo = mid
            else:
                hi = mid - 1
        if not possible_with_dist(intervals, lo):
            return None
        return lo

    return upper_bound(intervals)