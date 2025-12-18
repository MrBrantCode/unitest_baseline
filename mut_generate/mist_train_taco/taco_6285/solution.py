"""
QUESTION:
Given a sorted array A[] of N distinct integers from 0 to 99999. Find all the integer intervals missing from the given list.
Note: There is always atleast 1 number missing.
Example 1:
Input:
N = 4
A = {1,5,67,88}
Output:
0,2-4,6-66,68-87,89-99999
Explanation:
All the missing Intervals are printed.
Example 2: 
Input:
N = 6
A = {4,55,77,89,91,99} 
Output:
0-3,5-54,56-76,78-88,90,92-98, 100-99999
Your Task:  
You don't need to read input or print anything. Your task is to complete the function printMissingIntervals() which takes Integer N and an Array A[] as input and returns a array of elements with 2*x elements where x is the number of missing intervals and each pair in the array is the range missing. arr={1,3,97,100} would mean the intervals missing are 1-3 and 97-100. Suppose only the number 1 is missing ,then arr={1,1}.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 ≤ N ≤ 10^{5}
0 ≤ A_{i} < 10^{5}
"""

def find_missing_intervals(A, N):
    # Initialize a list to mark the presence of numbers in the range 0 to 99999
    presence = [0] * 100000
    
    # Mark the numbers present in the array
    for num in A:
        presence[num] = 1
    
    # Initialize the result list
    result = []
    curr = 0
    
    # Traverse the presence list to find missing intervals
    while curr < 100000:
        if presence[curr] == 0:
            start = curr
            # Find the end of the missing interval
            while curr < 100000 and presence[curr] == 0:
                curr += 1
            end = curr - 1
            # Append the interval to the result list
            result.append(start)
            result.append(end)
        else:
            curr += 1
    
    return result