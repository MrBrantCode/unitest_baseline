"""
QUESTION:
Given an array arr of size N, the goal is to find out the smallest number that is repeated exactly ‘K’ times.
 
Example 1:
Input:
N=5, K=2
arr[] = { 2 2 1 3 1 }
Output: 1
Explanation: Here in array,
2 is repeated 2 times, 1 is repeated
2 times, 3 is repeated 1 time.
Hence 2 and 1 both are repeated 'k' 
times i.e 2 and min(2, 1) is 1 .
 
Example 2:
Input:
N=4, K=1 
arr[] = { 3 5 3 2 }
Output:  2 
Explanation: Both 2 and 5 are repeating 1
time but min(5, 2) is 2.
 
Your Task:
You just need to complete the function findDuplicate() that takes array arr, integer N and integer K as parameters and returns the required answer.
Note- If there is no such element then return -1.
 
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(MAX). where MAX is maximum element in the array.
 
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ arr[i] ≤ 10^{5}
"""

def find_smallest_repeated_number(arr, N, K):
    # Create a dictionary to count occurrences of each number
    count_dict = {}
    
    # Count the occurrences of each number in the array
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Find the smallest number that is repeated exactly K times
    smallest_repeated_number = float('inf')
    found = False
    
    for num, count in count_dict.items():
        if count == K and num < smallest_repeated_number:
            smallest_repeated_number = num
            found = True
    
    # If no such number is found, return -1
    if not found:
        return -1
    
    return smallest_repeated_number