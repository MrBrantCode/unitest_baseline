"""
QUESTION:
There is a one-dimensional garden of length N. In each position of the N length garden, a sprinkler has been installed. Given an array a[]such that a[i] describes the coverage limit of the i^{th} sprinkler. A sprinkler can cover the range from the position max(i - a[i], 1) to min(i + a[i], N). In beginning, all the sprinklers are switched off.
The task is to find the minimum number of sprinklers needed to be activated such that the whole N-length garden can be covered by water.
Note:  Array is 1-based indexed.
Example 1:
Input: a[] = {1, 2, 1}
Output: 1
Explanation:
For position 1: a[1] = 1, range = 1 to 2
For position 2: a[2] = 2, range = 1 to 3
For position 3: a[3] = 1, range = 2 to 3
Therefore, the fountain at position a[2] covers
the whole garden. Therefore, the required output is 1.
Example 2:
Input: a[] = {2, 1, 1, 2, 1} 
Output: 2 
Explanation: 
For position 1: a[1] = 2, range = 1 to 3
For position 2: a[2] = 1, range = 1 to 3
For position 3: a[3] = 1, range = 2 to 4
For position 3: a[4] = 2, range = 2 to 5
For position 3: a[5] = 1, range = 4 to 5
Therefore, the fountain at position a[1] and a[4] covers the whole garden. Therefore, the required output is 2. Also possible answer is a[2] and a[4].
Your Task:
Your task is to complete the function minSprinkler() which takes an integer array a and an integer N as the input parameters and returns an integer denoting the minimum number of sprinkler needed to be activated such that the whole N-length garden can be covered by water.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
	1 <= N <= 2*10^{5}
	1 <= arr[i] <= 10^{9}
"""

def min_sprinklers(arr, N):
    coverages = [-1] * N
    for (i, a) in enumerate(arr):
        min_coverage = max(0, i - a)
        max_coverage = min(i + a, N - 1)
        coverages[min_coverage] = max(coverages[min_coverage], max_coverage)
    
    needed_sprinklers_count = 0
    current_coverage = -1
    next_max_coverage = -1
    
    for (i, max_cov) in enumerate(coverages):
        next_max_coverage = max(next_max_coverage, max_cov)
        if i > current_coverage:
            needed_sprinklers_count += 1
            current_coverage = next_max_coverage
    
    return needed_sprinklers_count