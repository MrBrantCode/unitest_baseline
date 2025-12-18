"""
QUESTION:
Given an array arr[] of N weights. Find the least weight capacity of a boat to ship all weights within D days.
The i^{th} weight has a weight of arr[i]. Each day, we load the boat with weights given by arr[i].We may not load more weight than the maximum weight capacity of the ship.
Note: You have to load weights on the boat in the given order.
 
Example 1:
Input:
N = 3
arr[] = {1, 2, 1}
D = 2
Output:
3
Explanation:
We can ship the weights in 2 days
in the following way:-
Day 1- 1,2
Day 2- 1
Example 2:
Input:
N = 3
arr[] = {9, 8, 10}
D = 3
Output:
10
Explanation:
We can ship the weights in 3 days
in the following way:-
Day 1- 9
Day 2- 8
Day 3- 10
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function leastWeightCapacity() which takes 2 integers N, and D, and an array arr of size N as input and returns the least weight capacity of the boat required.
Expected Time Complexity: O(N*log(Sum of weights - max(list of weights))
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ D ≤ N ≤ 10^{5}
1 ≤ arr[i] ≤ 500
"""

def least_weight_capacity(arr, N, D):
    def possible(arr, c, D):
        days_required = 1
        current_load = 0
        for weight in arr:
            current_load += weight
            if current_load > c:
                days_required += 1
                current_load = weight
        return days_required <= D
    
    total = 0
    max_load = 0
    for weight in arr:
        total += weight
        max_load = max(max_load, weight)
    
    left = max_load
    right = total
    
    while left < right:
        mid = (left + right) // 2
        if possible(arr, mid, D):
            right = mid
        else:
            left = mid + 1
    
    return left