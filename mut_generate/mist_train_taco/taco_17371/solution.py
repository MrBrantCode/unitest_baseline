"""
QUESTION:
N light bulbs are connected by a wire. Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb. Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs. "0 represents the bulb is off and 1 represents the bulb is on."
 
Example 1:
Input:
N=4
arr[] = { 0, 0, 0, 0 }
Output:  1
Explanation: 
From the given set of bulbs change
the state of the first bulb from off
to on ,which eventually turn the rest
three bulbs on the right of it.
Example 2:
Input:
N=4
arr[] = { 1, 0, 0, 1 }
Output:  2
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function countFlips() that takes array A and integer N as parameters and returns the minimum number of press required to turn on all the bulbs.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{6}
"""

def min_switches_to_turn_on_bulbs(bulbs, n):
    count = 0
    for i in range(n):
        if bulbs[i] == 1 and count % 2 == 0:
            continue
        elif bulbs[i] == 0 and count % 2 != 0:
            continue
        elif bulbs[i] == 1 and count % 2 != 0:
            count += 1
        elif bulbs[i] == 0 and count % 2 == 0:
            count += 1
    return count