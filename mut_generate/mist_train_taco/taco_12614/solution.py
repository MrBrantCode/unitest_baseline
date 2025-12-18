"""
QUESTION:
Given heights h[] of N towers, the task is to bring every tower to the same height by either adding or removing blocks in a tower. Every addition or removal operation costs cost[] a particular value for the respective tower. Find out the Minimum cost to Equalize the Towers.
Example 1:
Input: N = 3, h[] = {1, 2, 3} 
cost[] = {10, 100, 1000}
Output: 120
Explanation: The heights can be equalized 
by either "Removing one block from 3 and 
adding one in 1" or "Adding two blocks in 
1 and adding one in 2". Since the cost 
of operation in tower 3 is 1000, the first 
process would yield 1010 while the second 
one yields 120. Since the second process 
yields the lowest cost of operation, it is 
the required output.
 
Example 2:
Input: N = 5, h[] = {9, 12, 18, 3, 10} 
cost[] = {100, 110, 150, 25, 99}
Output: 1623 
 
Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function Bsearch() that takes integer N, array H, and array Cost as parameters and returns the minimum cost required to equalize the towers.
 
Expected Time Complexity: O(NlogN). 
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 10^{6}
"""

def minimum_cost_to_equalize_towers(N, heights, costs):
    def total_cost(mid, heights, costs):
        total_cost = 0
        for i in range(len(heights)):
            total_cost += abs(mid - heights[i]) * costs[i]
        return total_cost

    l = min(heights)
    r = max(heights)
    ans = float('inf')

    while l <= r:
        mid = (l + r) // 2
        lc = total_cost(mid - 1, heights, costs)
        pc = total_cost(mid, heights, costs)
        if lc >= pc:
            ans = pc
            l = mid + 1
        else:
            r = mid - 1

    return ans