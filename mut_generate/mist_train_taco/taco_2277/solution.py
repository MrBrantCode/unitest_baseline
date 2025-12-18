"""
QUESTION:
Given an array A[] of N positive integers which can contain integers from 1 to P where elements can be repeated or can be absent from the array. Your task is to count the frequency of all elements from 1 to N.
Note: The elements greater than N in the array can be ignored for counting and do modify the array in-place.
Example 1:
Input:
N = 5
arr[] = {2, 3, 2, 3, 5}
P = 5
Output:
0 2 2 0 1
Explanation: 
Counting frequencies of each array element
We have:
1 occurring 0 times.
2 occurring 2 times.
3 occurring 2 times.
4 occurring 0 times.
5 occurring 1 time.
Example 2:
Input:
N = 4
arr[] = {3,3,3,3}
P = 3
Output:
0 0 4 0
Explanation: 
Counting frequencies of each array element
We have:
1 occurring 0 times.
2 occurring 0 times.
3 occurring 4 times.
4 occurring 0 times.
Your Task:
You don't need to read input or print anything. Complete the function frequencycount() that takes the array and n as input parameters and modify the array itself in place to denote the frequency count of each element from 1 to N. i,e element at index 0 should represent the frequency of 1, and so on.
Can you solve this problem without using extra space (O(1) Space)?
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ P ≤ 4*10^{4}^{ }
1 <= A[i] <= P
"""

def frequency_count(arr, N, P):
    # Initialize a dictionary to count frequencies
    frequency_dict = {}
    
    # Count the frequency of each element in the array
    for num in arr:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    
    # Modify the array in place to represent the frequency count from 1 to N
    for i in range(1, N + 1):
        if i in frequency_dict:
            arr[i - 1] = frequency_dict[i]
        else:
            arr[i - 1] = 0
    
    return arr