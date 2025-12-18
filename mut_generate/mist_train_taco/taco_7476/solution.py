"""
QUESTION:
In some other world, today is Christmas Eve.
There are N trees planted in Mr. Takaha's garden. The height of the i-th tree (1 \leq i \leq N) is h_i meters.
He decides to choose K trees from these trees and decorate them with electric lights. To make the scenery more beautiful, the heights of the decorated trees should be as close to each other as possible.
More specifically, let the height of the tallest decorated tree be h_{max} meters, and the height of the shortest decorated tree be h_{min} meters. The smaller the value h_{max} - h_{min} is, the better. What is the minimum possible value of h_{max} - h_{min}?

-----Constraints-----
 - 2 \leq K < N \leq 10^5
 - 1 \leq h_i \leq 10^9
 - h_i is an integer.

-----Input-----
Input is given from Standard Input in the following format:
N K
h_1
h_2
:
h_N

-----Output-----
Print the minimum possible value of h_{max} - h_{min}.

-----Sample Input-----
5 3
10
15
11
14
12

-----Sample Output-----
2

If we decorate the first, third and fifth trees, h_{max} = 12, h_{min} = 10 so h_{max} - h_{min} = 2. This is optimal.
"""

def find_min_height_diff(N, K, heights):
    # Sort the heights list
    heights.sort()
    
    # Initialize the minimum difference to a large number
    min_diff = float('inf')
    
    # Iterate over the possible starting points of the subarray of length K
    for i in range(N - K + 1):
        # Calculate the difference between the max and min heights in the current subarray
        current_diff = heights[i + K - 1] - heights[i]
        
        # Update the minimum difference if the current one is smaller
        if current_diff < min_diff:
            min_diff = current_diff
    
    return min_diff