"""
QUESTION:
Given two unsorted arrays arr1[] and arr2[]. They may contain duplicates. For each element in arr1[] count elements less than or equal to it in array arr2[].
Example 1:
Input:
m = 6, n = 6
arr1[] = {1,2,3,4,7,9}
arr2[] = {0,1,2,1,1,4}
Output: 4 5 5 6 6 6
Explanation: Number of elements less than
or equal to 1, 2, 3, 4, 7, and 9 in the
second array are respectively 4,5,5,6,6,6
Example 2:
Input:
m = 5, n = 7
arr1[] = {4,8,7,5,1}
arr2[] = {4,48,3,0,1,1,5}
Output: 5 6 6 6 3
Explanation: Number of elements less than
or equal to 4, 8, 7, 5, and 1 in the
second array are respectively 5,6,6,6,3
Your Task :
Complete the function countEleLessThanOrEqual() that takes two array arr1[], arr2[],  m, and n as input and returns an array containing the required results(the count of elements less than or equal to it in arr2 for each element in arr1 where i_{th} output represents the count for i_{th} element in arr1.)
Expected Time Complexity: O((m + n) * log n).
Expected Auxiliary Space: O(m).
Constraints:
1<=m,n<=10^5
0<=arr1[i],arr2[j]<=10^5
"""

def count_elements_less_than_or_equal(arr1, arr2):
    # Determine the maximum value in both arrays
    max_val = max(max(arr1), max(arr2))
    
    # Initialize a holder array to count occurrences of each element in arr2
    holder = [0] * (max_val + 1)
    
    # Count occurrences of each element in arr2
    for num in arr2:
        holder[num] += 1
    
    # Convert holder array to a cumulative count array
    count = 0
    for i in range(len(holder)):
        count += holder[i]
        holder[i] = count
    
    # Replace each element in arr1 with the count of elements in arr2 less than or equal to it
    for i in range(len(arr1)):
        arr1[i] = holder[arr1[i]]
    
    return arr1