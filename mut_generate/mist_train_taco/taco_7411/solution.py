"""
QUESTION:
Given an array of n integers and q queries. Write a program to find floor value of mean in range l to r for each query in a new line.
Queries are given by an array queries[] of size 2*q. Here queries[2*i] denote l and queries[2*i+1] denote r for i-th query (0<= i <q).
Example 1:
Input : Arr[] = {1, 2, 3, 4, 5}, Q = 3
queries[] = {0, 2, 1, 3, 0, 4}
Output : 2 3 3
Explanation:
Here we can see that the array of 
integers is [1, 2, 3, 4, 5].
Query 1: L = 0 and R = 2
Sum = 6
Integer Count = 3
So, Mean is 2
Query 2: L = 1 and R = 3
Sum = 9
Integer Count = 3
So, Mean is 3
Query 3: L = 0 and R = 4
Sum = 15
Integer Count = 5
So, the Mean is 3.
So, In the end, the function will 
return the array [2, 3, 3] as an answer.
Example 2:
Input : Arr[] = {6, 7, 8, 10}, Q = 2
queries[] = {0, 3, 1, 2}
Output : 7 7
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function findMean() that takes an array (arr), an array of queries (queries), sizeOfArray (n), sizeOfQueriesArray (2*q) and return the array of size q which has the answer for all the queries. The driver code takes care of the printing.
Expected Time Complexity: O(q + n).
Expected Auxiliary Space: O(n).
Constraints: 
1 ≤ q,n ≤ 2*10^{5}
1 ≤ a[i] ≤ 10^{3}
"""

def calculate_floor_means(arr, queries):
    n = len(arr)
    q = len(queries) // 2
    
    # Create a prefix sum array
    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    
    results = []
    for i in range(0, len(queries), 2):
        l = queries[i]
        r = queries[i + 1]
        
        if l == 0:
            sum_range = prefix_sum[r]
        else:
            sum_range = prefix_sum[r] - prefix_sum[l - 1]
        
        count = r - l + 1
        mean_floor = sum_range // count
        results.append(mean_floor)
    
    return results