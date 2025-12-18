"""
QUESTION:
Given an array of items, the i'th index element denotes the item id’s and given a number m, the task is to remove m elements such that there should be minimum distinct id’s left. Print the number of distinct id’s.
Example 1 -
Input:
n = 6
arr[] = {2, 2, 1, 3, 3, 3}
m = 3
Output:
1
Explanation : 
Remove 2,2,1
Example 2 -
Input:
n = 8
arr[] = {2, 4, 1, 5, 3, 5, 1, 3}
m = 2
Output:
3
Explanation:
Remove 2,4
Your Task:
This is a function problem. You don't have to take any input. Your task is to complete the distinctIds() which takes sorted array, its size n, and m as its parameter. You only need to find the minimum number of distinct IDs and return it. The driver code will print the returned value.
Expected Time Complexity: O(n log(n))
Expected Auxillary Space: O(n)
Constraints:
1 ≤ n ≤ 10^{5}
1 ≤ arr[i] ≤ 10^{6}
1 ≤ m ≤ 10^{3}
"""

from collections import defaultdict

def minimum_distinct_ids(arr: list, m: int) -> int:
    mp = defaultdict(int)
    count = 0
    
    # Count the frequency of each item id
    for i in arr:
        mp[i] += 1
    
    # Create a list of frequencies
    frequencies = list(mp.values())
    
    # Sort the frequencies in ascending order
    frequencies.sort()
    
    # Calculate the number of distinct ids after removing m elements
    for freq in frequencies:
        if freq <= m:
            m -= freq
            count += 1
        else:
            break
    
    # Return the number of distinct ids left
    return len(frequencies) - count