"""
QUESTION:
Motu and Patlu are playing with a Magical Ball. Patlu find some interesting pattern in the motion of the ball that ball always bounce back from the ground after travelling a linear distance whose value is some power of $2$. Patlu gave Motu total distance $D$ travelled by the ball and ask him to calculate the minimum number of bounces that the ball makes before coming to rest.

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- Each testcase contains of a single line of input, single integers $D$.
- Note : Power of $2$ must be a non-negative integer. 

-----Output:-----
For each testcase, output in a single line answer, the minimum number of bounces the ball makes before coming to rest.

-----Constraints-----
- $1 \leq T \leq 10^5$
- $1$ $\leq$ $M$< $10$^18

-----Sample Input:-----
1
13 

-----Sample Output:-----
2

-----EXPLANATION:-----
"""

def calculate_minimum_bounces(D: int) -> int:
    """
    Calculate the minimum number of bounces a ball makes before coming to rest, given the total distance D.

    Parameters:
    D (int): The total distance travelled by the ball.

    Returns:
    int: The minimum number of bounces the ball makes before coming to rest.
    """
    # Convert the distance to its binary representation
    binary_representation = bin(D)
    
    # Count the number of '1's in the binary representation
    num_ones = binary_representation.count('1')
    
    # The minimum number of bounces is the count of '1's minus 1
    return num_ones - 1