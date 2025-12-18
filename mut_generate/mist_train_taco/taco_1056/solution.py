"""
QUESTION:
Sorting is useful as the first step in many different tasks. The most common task is to make finding things easier, but there are other uses as well.  In this case, it will make it easier to determine which pair or pairs of elements have the smallest absolute difference between them.

Example 

$arr=[5,2,3,4,1]$   

Sorted, $ar r'=[1,2,3,4,5]$.  Several pairs have the minimum difference of $1$: $[(1,2),(2,3),(3,4),(4,5)]$.  Return the array $[1,2,2,3,3,4,4,5]$.

Note 

As shown in the example, pairs may overlap.  

Given a list of unsorted integers, $\textbf{arr}$, find the pair of elements that have the smallest absolute difference between them. If there are multiple pairs, find them all.

Function Description  

Complete the closestNumbers function in the editor below.   

closestNumbers has the following parameter(s):  

int arr[n]: an array of integers   

Returns 

- int[]: an array of integers as described   

Input Format

The first line contains a single integer $n$, the length of $\textbf{arr}$. 

The second line contains $n$ space-separated integers, $arr\left[i\right]$.

Constraints

$2\leq n\leq200000$
$-10^7\leq arr[i]\leq10^7$
All $a[i]$ are unique in $\textbf{arr}$.

Output Format

Sample Input 0

10
-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 

Sample Output 0

-20 30

Explanation 0 

(30) - (-20) = 50, which is the smallest difference.  

Sample Input 1

12
-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 -520 -470 

Sample Output 1

-520 -470 -20 30

Explanation 1 

(-470) - (-520) = 30 - (-20) = 50, which is the smallest difference. 

Sample Input 2

4
5 4 3 2

Sample Output 2

2 3 3 4 4 5

Explanation 2 

Here, the minimum difference is 1. Valid pairs are (2, 3), (3, 4), and (4, 5).
"""

def closest_numbers(arr):
    # Step 1: Sort the array
    sorted_arr = sorted(arr)
    
    # Step 2: Initialize variables to track the minimum difference and the result pairs
    min_diff = float('inf')
    result = []
    
    # Step 3: Iterate through the sorted array to find the pairs with the smallest difference
    for i in range(1, len(sorted_arr)):
        diff = abs(sorted_arr[i] - sorted_arr[i - 1])
        if diff < min_diff:
            # Update the minimum difference and reset the result list
            min_diff = diff
            result = [sorted_arr[i - 1], sorted_arr[i]]
        elif diff == min_diff:
            # Append the pair to the result list if the difference is the same as the minimum
            result.extend([sorted_arr[i - 1], sorted_arr[i]])
    
    # Step 4: Return the result list
    return result