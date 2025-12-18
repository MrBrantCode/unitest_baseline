"""
QUESTION:
Given a number N denoting candies. Find how many packets are needed to contain the number if 1st packet can contain 1 candy, 2nd packet can contain 2 candies, 3rd packet can contain 4 candies and so on.
Example 1:
Input:
N = 2
Output:
2
Explanation:
Put 1 candy in first packet.
Put 1 candy in second packet.
Thus two,packets are required.
Example 2:
Input:
N = 8
Output:
4
Explanation:
Put 1 candy in first packet.
Put 2 candies in second packet.
Put 4 candies in third packet.
Put 1 candy in fourth packet.
Thus 4 packets are required.
Your Task:
You don't need to read input or print anything.Your Task is to complete the function countPackets() which takes a number N as input parameter and returns the number of packets required to contain it.
Expected Time Complexity:O(logN)
Expected Auxillary Space:O(1)
Constraints:
1<= N <= 10^{18}
"""

def count_packets(N: int) -> int:
    c = 0
    while N:
        N //= 2
        c += 1
    return c