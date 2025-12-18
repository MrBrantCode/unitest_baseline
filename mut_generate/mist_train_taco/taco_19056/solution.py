"""
QUESTION:
Sidddharth is very kind-hearted. He doesn't want to give you any stupid problem statement that wastes your time.

Given an array of integers, find the sum of the ith largest and jth smallest number from the array.

Input Format:
First line of the input consists of a single integer T, number of test cases.
Each test case has 3 lines as input.
First line will have a single integer N, denoting number of elements in array(A).
Next line contains N integers.
Last line consists of integers i & j.  

Output Format:
Print the required sum or for each test case 

Constraints:
1 ≤ T ≤ 10
1 ≤ N ≤ 1000
1 ≤ A[i] ≤ 10^6
1 ≤ i,j ≤ n 

Problem Setter : Siddharth Seth

SAMPLE INPUT
1
8
1 2 5 3 6 4 8 7
3 4

SAMPLE OUTPUT
10
"""

def sum_ith_largest_and_jth_smallest(arr, i, j):
    # Sort the array to easily find the ith largest and jth smallest
    sorted_arr = sorted(arr)
    
    # Find the jth smallest element (0-based index)
    jth_smallest = sorted_arr[j-1]
    
    # Find the ith largest element (0-based index from the end)
    ith_largest = sorted_arr[-(i)]
    
    # Return the sum of the ith largest and jth smallest
    return jth_smallest + ith_largest