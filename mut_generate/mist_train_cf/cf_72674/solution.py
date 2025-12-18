"""
QUESTION:
Find the smallest positive integer missing from a 2D array where the elements are arranged in either non-increasing or non-decreasing order across both horizontal and vertical axes. The function should be named `find_smallest_pos_int` and it should accept a 2D array `arr` as input. The solution should have a time complexity of O(n^2) and a space complexity of O(1), where n is the number of rows in the array. The function should handle arrays with duplicate numbers, and it should also work for arrays that exclusively contain negative integers or zeros.
"""

def find_smallest_pos_int(arr):
    n = len(arr)
    if n==0:
        return 1
    
    m = len(arr[0])
    
    if (arr[0][0]==1 or arr[n-1][m-1]==1): 
        return 2

    sm_pos_int = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j]>0 and arr[i][j]<=sm_pos_int:
                sm_pos_int+=1
                
    return sm_pos_int