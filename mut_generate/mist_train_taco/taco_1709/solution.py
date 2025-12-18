"""
QUESTION:
A total of n depots are located on a number line. Depot i lies at the point x_i for 1 ≤ i ≤ n.

You are a salesman with n bags of goods, attempting to deliver one bag to each of the n depots. You and the n bags are initially at the origin 0. You can carry up to k bags at a time. You must collect the required number of goods from the origin, deliver them to the respective depots, and then return to the origin to collect your next batch of goods.

Calculate the minimum distance you need to cover to deliver all the bags of goods to the depots. You do not have to return to the origin after you have delivered all the bags.

Input

Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10 500). Description of the test cases follows.

The first line of each test case contains two integers n and k (1 ≤ k ≤ n ≤ 2 ⋅ 10^5).

The second line of each test case contains n integers x_1, x_2, …, x_n (-10^9 ≤ x_i ≤ 10^9). It is possible that some depots share the same position.

It is guaranteed that the sum of n over all test cases does not exceed 2 ⋅ 10^5.

Output

For each test case, output a single integer denoting the minimum distance you need to cover to deliver all the bags of goods to the depots. 

Example

Input


4
5 1
1 2 3 4 5
9 3
-5 -10 -15 6 5 8 3 7 4
5 3
2 2 3 3 3
4 2
1000000000 1000000000 1000000000 1000000000


Output


25
41
7
3000000000

Note

In the first test case, you can carry only one bag at a time. Thus, the following is a solution sequence that gives a minimum travel distance: 0 → 2 → 0 → 4 → 0 → 3 → 0 → 1 → 0 → 5, where each 0 means you go the origin and grab one bag, and each positive integer means you deliver the bag to a depot at this coordinate, giving a total distance of 25 units. It must be noted that there are other sequences that give the same distance.

In the second test case, you can follow the following sequence, among multiple such sequences, to travel minimum distance: 0 → 6 → 8 → 7 → 0 → 5 → 4 → 3 → 0 → (-5) → (-10) → (-15), with distance 41. It can be shown that 41 is the optimal distance for this test case.
"""

def calculate_minimum_delivery_distance(n, k, depot_positions):
    positive_positions = []
    negative_positions = []
    
    # Separate the positions into positive and negative lists
    for pos in depot_positions:
        if pos > 0:
            positive_positions.append(pos)
        else:
            negative_positions.append(pos)
    
    total_distance = 0
    
    # Process positive positions
    if positive_positions:
        positive_positions.sort()
        for i in range(len(positive_positions) - 1, -1, -k):
            total_distance += positive_positions[i] * 2
    
    # Process negative positions
    if negative_positions:
        negative_positions.sort()
        negative_positions = negative_positions[::-1]  # Reverse to process from the largest negative
        for i in range(len(negative_positions) - 1, -1, -k):
            total_distance -= negative_positions[i] * 2
    
    # Adjust the total distance to avoid returning to the origin after the last delivery
    if not positive_positions:
        total_distance += negative_positions[-1]
    elif not negative_positions:
        total_distance -= positive_positions[-1]
    else:
        total_distance -= max(-negative_positions[-1], positive_positions[-1])
    
    return total_distance