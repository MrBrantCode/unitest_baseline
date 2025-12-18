"""
QUESTION:
Given an array arr[] of n numbers. The task is to print only those numbers whose digits are from set {1,2,3}.
Example 1:
Input:
n = 3
arr[] = {4,6,7}
Output: -1
Explanation: No elements are there in the 
array which contains digits 1, 2 or 3.
Example 2:
Input:
n = 4
arr[] = {1,2,3,4}
Output: 1 2 3
Explanation: 1, 2 and 3 are the only 
elements in the array which conatins 
digits as 1, 2 or 3.
Your Task:
Complete findAll function and marked satisfied number as '1' in the map mp in range 1 to 1000000. If no number is marked as satified number -1 will automatically be printed by the drivers code. The driver code prints the elements in sorted order.
Expected Time Complexity : O(n)
Expected Auxilliary Space : O(n)
Constraints:
1 <= n <= 10^{6}
1 <= A[i] <= 10^{6}
"""

def filter_numbers_by_digits(arr, n):
    # Set of allowed digits
    allowed_digits = {'1', '2', '3'}
    
    # Result list to store numbers that meet the criteria
    result = []
    
    # Iterate through each number in the array
    for num in arr:
        # Convert the number to a string and create a set of its digits
        num_digits = set(str(num))
        
        # Check if all digits of the number are in the allowed_digits set
        if num_digits.issubset(allowed_digits):
            result.append(num)
    
    # If no numbers meet the criteria, return [-1]
    if not result:
        return [-1]
    
    # Return the filtered list of numbers
    return result