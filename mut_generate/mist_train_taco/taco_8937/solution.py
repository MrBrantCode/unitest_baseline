"""
QUESTION:
Given N piles of bananas, the ith pile has piles[i] bananas and H hours time until guards return (N <= H). Find the minimum (S) bananas to eat per hour such that Koko can eat all the bananas within H hours. Each hour, Koko chooses some pile of bananas and eats S bananas from that pile. If the pile has less than S bananas, then she consumes all of them, and wont eat any more bananas during that hour. 
Example 1:
Input:
n = 4
piles = [3, 6, 7, 11]
H = 8
Output:
4
Example 2:
Input:
n = 5
piles = [30, 11, 23, 4, 20]
H = 5
Output:
30
Your Task:
You don't need to read input or print anything. Your task is to complete the function Solve() which takes an integer n and a list of piles and integer H denoting Hour and return the minimum bananas to eat per hour.
Constraint:
1 <= n <= 10^{4 }
1 <= piles[i] <= 10^{9 }
n <= H <= 10^{4}
"""

def find_min_eating_speed(piles, H):
    low, high = 1, max(piles) + 1
    while low < high:
        mid = (low + high) // 2
        count = 0
        for p in piles:
            count += (p + mid - 1) // mid
        if count > H:
            low = mid + 1
        else:
            high = mid
    return low