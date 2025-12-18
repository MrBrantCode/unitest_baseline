"""
QUESTION:
We have an horizontal number line. On that number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = size of the stations array. Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized. We have to find the smallest possible value of D. Find the answer exactly to 2 decimal places.
Example 1:
Input:
N = 10
stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 9
Output: 0.50
Explanation: Each of the 9 stations can be added mid way between all the existing adjacent stations.
Example 2:
Input:
N = 10
stations = [3,6,12,19,33,44,67,72,89,95]
K = 2
Output: 14.00
Explanation: Construction of gas stations at 86 locations
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function findSmallestMaxDist() which takes a list of stations and integer K as inputs and returns the smallest possible value of D. Find the answer exactly to 2 decimal places.
Expected Time Complexity: O(N*log K)
Expected Auxiliary Space: O(1)
Constraint:
10 <= N <= 5000^{ }
0 <= stations[i] <= 10^{9 }
0 <= K <= 10^{5}
stations is sorted in a strictly increasing order.
"""

def find_smallest_max_dist(stations, K):
    def is_possible(stations, k, max_dist):
        stations_to_add = 0
        for i in range(1, len(stations)):
            stations_to_add += (stations[i] - stations[i - 1]) // max_dist
        return stations_to_add <= k

    start, end = 0, stations[-1] - stations[0]
    while end - start > 1e-05:
        mid = (start + end) / 2
        if is_possible(stations, K, mid):
            end = mid
        else:
            start = mid
    return round(end, 2)