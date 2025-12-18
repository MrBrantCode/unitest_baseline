"""
QUESTION:
Given an array, the task is to find the difference between highest occurrence and lowest occurrence of any number in an array.
Note: If only one type of element is present in the array return 0.
 
Example 1:
Input:
arr[] = [1, 2, 2]
Output:
1
Explanation:
Lowest occurring element (1) occurs once.
Highest occurring element (2) occurs 2 times
 
Example 2:
Input : 
arr[] = [7, 8, 4, 5, 4, 1, 1, 7, 7, 2, 5]
Output : 
2
Explanation :
Lowest occurring element (2) occurs once.
Highest occurring element (7) occurs 3 times
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function leftElement() which takes the array arr[] and its size N as inputs and returns the difference between highest occurrence and lowest occurrence of any number in the array.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1<=N<=10^{5}
1<=A[i]<=10^{5}
"""

def find_occurrence_difference(arr, n):
    # Dictionary to store the frequency of each element
    frequency_dict = {}
    
    # Count the occurrences of each element in the array
    for num in arr:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    
    # Get the values (frequencies) from the dictionary
    frequencies = frequency_dict.values()
    
    # Calculate the difference between the highest and lowest occurrence
    if len(frequencies) == 1:
        return 0
    else:
        return max(frequencies) - min(frequencies)