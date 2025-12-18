"""
QUESTION:
Given N students sitting in a circle, distribute M candies to these students. The i_{th} student can take only i candies. If i_{th} student does not get the required amount of candies he will not take it. Distribute the candies starting from the 1st student and moving along the circle of students till you reach a student you can not give candies to. You need to find the amount of candies left.
Example 1:
Input:
N = 4, M = 11
Output: 0
Explanation: You first give 1 candy to 1st student, 
2 to 2nd , 3 to 3rd , 4 to 4th then again 1 to first. 
All candies are finished with none left out.
Example 2:
Input:
N = 4, M = 12
Output: 1
Explanation: You are left with only one candy.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function leftCandies() which takes two integers n and m as input parameters and returns an integer denoting the amount of candies left.
 
Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)
 
Constraints:
1 ≤ N ≤ 10^{9}
1 ≤ M ≤ 10^{18}
"""

def leftCandies(n, m):
    # Calculate the total number of candies required to complete one full cycle
    total_candies_per_cycle = n * (n + 1) // 2
    
    # Calculate the remainder of candies after completing full cycles
    candy_left = m % total_candies_per_cycle
    
    # Binary search to find the maximum number of students who can get their required candies
    start = 0
    end = n
    while start <= end:
        mid = (start + end) // 2
        curr = mid * (mid + 1) // 2
        if curr == candy_left:
            return 0
        elif curr > candy_left:
            end = mid - 1
        else:
            start = mid + 1
    
    # Calculate the remaining candies after distributing to the maximum number of students
    return candy_left - end * (end + 1) // 2