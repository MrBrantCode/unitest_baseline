"""
QUESTION:
There are N people in a room. If two persons shake hands exactly once, find the maximum number of handshakes possible. 
 
Example 1:
Input: N = 2
Output: 1
Explaination: There are two people and they 
can shake hands maximum one time.
 
Example 2:
Input: N = 3
Output: 3
Explaination: Let the people be person 1, 2 and 3. 
So the possible handshakes are (1, 2), (2, 3) and 
(1, 3).
 
Your Task:
You do not need to read input or print anything. Your task is to complete the function handShakes() which takes N as input parameter and returns the maximum number of handshakes possible.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
2 ≤ N ≤ 10^{9}
"""

def calculate_max_handshakes(N: int) -> int:
    """
    Calculate the maximum number of handshakes possible among N people in a room.

    Parameters:
    N (int): The number of people in the room.

    Returns:
    int: The maximum number of handshakes possible.
    """
    return N * (N - 1) // 2