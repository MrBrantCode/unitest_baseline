"""
QUESTION:
In a flower bed, there are N flowers, numbered 1,2,......,N. Initially, the heights of all flowers are 0.
You are given a sequence h=\{h_1,h_2,h_3,......\} as input. You would like to change the height of Flower k to h_k for all k (1 \leq  k \leq N), by repeating the following "watering" operation:
 - Specify integers l and r. Increase the height of Flower x by 1 for all x such that l \leq x \leq r.
Find the minimum number of watering operations required to satisfy the condition.

-----Constraints-----
 - 1 \leq N  \leq 100
 - 0 \leq h_i \leq 100
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N
h_1 h_2 h_3 ...... h_N

-----Output-----
Print the minimum number of watering operations required to satisfy the condition.

-----Sample Input-----
4
1 2 2 1

-----Sample Output-----
2

The minimum number of watering operations required is 2.
One way to achieve it is:
 - Perform the operation with (l,r)=(1,3).
 - Perform the operation with (l,r)=(2,4).
"""

def minimum_watering_operations(N: int, h: list) -> int:
    """
    Calculate the minimum number of watering operations required to achieve the desired heights of flowers.

    Parameters:
    - N (int): The number of flowers.
    - h (list): A list of integers representing the desired heights of the flowers.

    Returns:
    - int: The minimum number of watering operations required.
    """
    s = h[0]
    for i in range(N - 1):
        if h[i] <= h[i + 1]:
            s += h[i + 1] - h[i]
    return s