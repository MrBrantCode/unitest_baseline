"""
QUESTION:
Given an array A. Delete an single element from the array such that sum of the differences of adjacent elements should be minimum.  

For more clarification Sum for an array A having N element is defined as :  
abs( A[0] - A[1] )  + abs( A[1] - A[2] ) + abs( A[2] - A[3] ) +............ + abs( A[N-2] - A[N-1] )    

Input:
First line contains number of test cases T. Each test cases contains two lines. First line contains an integer N, size of the array and second line contains N space separated elements of array A.   

Output:
For each test case print the index of the element in the array A, which if deleted, minimizes the value of the sum.. If there is multiple answer possible print the lowest index value.  

NOTE:
We are using is 0-based indexing for array.  

Constraints:
1 ≤ T ≤ 5
1<N ≤ 100000
1 ≤ Arri ≤ 10^9

SAMPLE INPUT
1
5
1 10 20 40 60

SAMPLE OUTPUT
4
"""

def find_min_diff_index(arr, n):
    if n < 3:
        return 0
    
    # Calculate the initial sum of differences
    initial_sum = sum(abs(arr[i] - arr[i + 1]) for i in range(n - 1))
    
    # Initialize variables to track the maximum reduction and the corresponding index
    max_reduction = 0
    min_index = 0
    
    # Check the impact of removing each element (except the first and last)
    for i in range(1, n - 1):
        current_reduction = abs(arr[i - 1] - arr[i]) + abs(arr[i] - arr[i + 1]) - abs(arr[i - 1] - arr[i + 1])
        if current_reduction > max_reduction:
            max_reduction = current_reduction
            min_index = i
    
    # Check the impact of removing the last element
    if n > 2 and abs(arr[n - 1] - arr[n - 2]) > max_reduction:
        min_index = n - 1
    
    return min_index