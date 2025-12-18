"""
QUESTION:
There are N temples in a straight line and K monks who want to spread  their enlightening power to the entire road of temples. All the monks have an enlightenment value, which denotes the range of enlightenment which they can spread in both the directions. Since, they do not want to waste their efficiency on trivial things of the world, they want to keep their range minimum.

Also, when we say that the N temples are in a straight line, we mean that that all the temples lie on something like an X-axis in a graph.

Find the minimum enlightenment value such that all the temples can receive it. 

Input Format:
The first line contains two integers, N and K - denoting the number of temples and number of monks.  The next line contains N integers denoting the position of the temples in the straight line.

Output format:
Print the answer in a new line.

Constraints:
1 ≤ N  ≤ 10^5
1 ≤ K < N 
1 ≤ Positioni ≤ 10^7

Update: 
The enlightenment value is an integer.

SAMPLE INPUT
3 2
1 5 20

SAMPLE OUTPUT
2

Explanation

The optimal answer is 2.
A monk positioned at 3, can serve temples at 1 and 5.
The other monk can be placed at 18, to serve temple at 20.
"""

def find_minimum_enlightenment(temple_positions, num_monks):
    def is_enlightenment_possible(ar, n, k, dist):
        # Checks if all n temples in list ar is possible to be enlightened by k monks with range dist
        pos = ar[0] + dist
        for i in ar:
            if abs(pos - i) > dist:
                k = k - 1
                pos = i + dist
        k = k - 1
        if k >= 0:
            return True
        return False

    temple_positions.sort()
    lo, hi = 1, 10000000
    ans = 0
    while lo <= hi:
        mid = (lo + hi) >> 1
        if is_enlightenment_possible(temple_positions, len(temple_positions), num_monks, mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans