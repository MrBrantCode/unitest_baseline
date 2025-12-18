"""
QUESTION:
Himu wants to go on a long drive with his girlfriend. There are N cities numbered from 1 to N, and every city is connected to every other city with bidirectional road. The length of a road is equal to XOR of the city numbers it is connecting. For example the length of road connecting city numbers 8 and 4 is 12. Himu wants this drive to be really long, so he will choose the road having maximum length. Help Himu find out the length of the longest road.

Input:
First line consists of T, the number of test cases.
Second line consists of N, the number of cities.

Output:
Print the answer for each test case in a new line.

Constraints:
1 ≤ T ≤ 10^5
1 ≤ N ≤ 10^9

SAMPLE INPUT
1
3

SAMPLE OUTPUT
3

Explanation

There are 3 cities.
Length of road between city number 1 & 2 = 3
Length of road between city number 2 & 3 = 1
Length of road between city number 1 & 3 = 2
So, clearly the maximum road length is  3.
"""

def find_longest_road_length(N):
    """
    Calculate the length of the longest road between any two cities.

    Parameters:
    N (int): The number of cities.

    Returns:
    int: The length of the longest road.
    """
    if N <= 1:
        return 0
    
    # The longest road length is the maximum XOR value between any two city numbers.
    # The maximum XOR value between any two numbers up to N is (N XOR (N-1)).
    # To find the maximum XOR value, we can use the highest bit set in N.
    
    # Find the highest bit set in N
    highest_bit = 1
    while highest_bit <= N:
        highest_bit <<= 1
    
    # The longest road length is the highest bit minus 1
    return highest_bit - 1