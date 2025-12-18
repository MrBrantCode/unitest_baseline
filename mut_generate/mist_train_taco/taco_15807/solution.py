"""
QUESTION:
Snuke has an integer sequence A of length N.
He will make three cuts in A and divide it into four (non-empty) contiguous subsequences B, C, D and E.
The positions of the cuts can be freely chosen.
Let P,Q,R,S be the sums of the elements in B,C,D,E, respectively.
Snuke is happier when the absolute difference of the maximum and the minimum among P,Q,R,S is smaller.
Find the minimum possible absolute difference of the maximum and the minimum among P,Q,R,S.

-----Constraints-----
 - 4 \leq N \leq 2 \times 10^5
 - 1 \leq A_i \leq 10^9
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N
A_1 A_2 ... A_N

-----Output-----
Find the minimum possible absolute difference of the maximum and the minimum among P,Q,R,S.

-----Sample Input-----
5
3 2 4 1 2

-----Sample Output-----
2

If we divide A as B,C,D,E=(3),(2),(4),(1,2), then P=3,Q=2,R=4,S=1+2=3.
Here, the maximum and the minimum among P,Q,R,S are 4 and 2, with the absolute difference of 2.
We cannot make the absolute difference of the maximum and the minimum less than 2, so the answer is 2.
"""

def find_min_abs_difference(N, A):
    # Calculate cumulative sums
    tmp = 0
    ca = [0]
    for ai in A:
        tmp += ai
        ca.append(tmp)
    
    from bisect import bisect_right, bisect_left
    
    ans = float('inf')
    f, g = 1, 3
    
    for i in range(2, N - 1):
        # Adjust the first cut position
        while abs(ca[i] - ca[f] - ca[f]) > abs(ca[i] - ca[f + 1] - ca[f + 1]):
            f += 1
        
        # Adjust the second cut position
        while abs(ca[-1] - ca[g] - (ca[g] - ca[i])) > abs(ca[-1] - ca[g + 1] - (ca[g + 1] - ca[i])):
            g += 1
        
        # Calculate the sums of the four subsequences
        l = (ca[f], ca[i] - ca[f], ca[-1] - ca[g], ca[g] - ca[i])
        
        # Update the minimum absolute difference
        ans = min(ans, max(l) - min(l))
    
    return ans