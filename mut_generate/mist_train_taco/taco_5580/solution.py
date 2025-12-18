"""
QUESTION:
Given an array arr[] of N values, the task is to find the number which has the maximum number of zeroes. If there are no zeroes then print -1.
Note: If there are multiple numbers with the same (max) number of zeroes then print the Maximum number among them.
Example 1:
Input: N = 5
arr[] = {10, 20, 3000, 9999, 200}
Output:  3000
Explanation: 3000 contains 3 zero's 
in it.
Example 2:
Input: N = 4
arr[] = {1, 2, 3, 4}
Output:  -1
Explanation: No zero is present.
 
Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function MaxZero() that takes array arr[] and integer N as parameters and returns the number with the maximum number of zeroes.
 
Expected Time Complexity: O(N*M). where N is the size of array and M is the maximum length of a number in the array
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{5}
1 < A[i] < 10^{100}
"""

def find_number_with_max_zeroes(arr, N):
    max_zeroes = -1
    result = -1
    
    for num in arr:
        str_num = str(num)
        zero_count = str_num.count('0')
        
        if zero_count > max_zeroes:
            max_zeroes = zero_count
            result = num
        elif zero_count == max_zeroes:
            if num > result:
                result = num
    
    return result