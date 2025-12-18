"""
QUESTION:
Find out the maximum sub-array of non negative numbers from an array. 

The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

NOTE 1 :If there is a tie, then compare with segment's length and return segment which has maximum length 

NOTE 2: If there is still a tie, then return the segment with minimum starting index.

-----Input-----

The first line contains the number of test cases. Each test cases contains an integer N. next line consists of N integers, the elements of the array.

-----Output-----

Print out the maximum sub-array as stated above.

-----Constraints-----
-  1  ≤  T  ≤  100 
-  1  ≤  N  ≤  105 
-  1  ≤  Ai  ≤  105 

-----Example-----
Input:

1
6
1 2 5 -7 2 3

Output:

1 2 5
"""

def find_max_non_negative_subarray(arr):
    n = len(arr)
    if n == 0:
        return [], -1, -1
    
    max_sum = -1
    max_length = 0
    max_start = 0
    max_end = 0
    
    current_sum = 0
    current_start = 0
    
    for i in range(n):
        if arr[i] >= 0:
            current_sum += arr[i]
        else:
            if current_sum > max_sum or (current_sum == max_sum and (i - current_start) > max_length):
                max_sum = current_sum
                max_length = i - current_start
                max_start = current_start
                max_end = i
            current_sum = 0
            current_start = i + 1
    
    # Check the last subarray if it ends at the end of the array
    if current_sum > max_sum or (current_sum == max_sum and (n - current_start) > max_length):
        max_sum = current_sum
        max_length = n - current_start
        max_start = current_start
        max_end = n
    
    max_subarray = arr[max_start:max_end]
    return max_subarray, max_start, max_end