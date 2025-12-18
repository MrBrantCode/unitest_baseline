"""
QUESTION:
You are given a list of integers nums where each number represents a vote to a candidate. Return the ids of the candidates that have greater than n/3 votes, If there's not a majority vote, return -1. 
Example 1:
Input:
n = 11
nums = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Output:
[5,6]
Explanation:
5 and 6 occur more n/3 times.
 
Example 2:
Input:
n=5
nums = [1,2,3,4,5]
Output:
[-1]
Your Task:
You don't need to read input or print anything. Your task is to complete the function Solve() which takes a integer n denoting a number of element and a list of numbers and return the list of number which occur more than n/3 time.
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)
Constraint:
1 <=  n  <= 5 * 10^{4}
-10^{9} <= nums[i] <= 10^{9}
"""

def find_majority_candidates(n, nums):
    count1, count2 = 0, 0
    element1, element2 = 0, 0
    
    for num in nums:
        if count1 == 0 and element2 != num:
            count1 += 1
            element1 = num
        elif num == element1:
            count1 += 1
        elif count2 == 0 and element1 != num:
            count2 += 1
            element2 = num
        elif num == element2:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
    
    final_answer = []
    final_count1, final_count2 = 0, 0
    
    for num in nums:
        if num == element1:
            final_count1 += 1
        if num == element2:
            final_count2 += 1
    
    if final_count1 > n // 3:
        final_answer.append(element1)
    if final_count2 > n // 3:
        final_answer.append(element2)
    
    return final_answer if final_answer else [-1]