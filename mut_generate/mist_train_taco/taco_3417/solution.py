"""
QUESTION:
Given two strings A and B. Find the minimum number of steps required to transform string A into string B. The only allowed operation for the transformation is selecting a character from string A and inserting it in the beginning of string A.
Example 1:
Input:
A = "abd"
B = "bad"
Output: 1
Explanation: The conversion can take place in
1 operation: Pick 'b' and place it at the front.
Example 2:
Input:
A = "GeeksForGeeks"
B = "ForGeeksGeeks"
Output: 3
Explanation: The conversion can take
place in 3 operations:
Pick 'r' and place it at the front.
A = "rGeeksFoGeeks"
Pick 'o' and place it at the front.
A = "orGeeksFGeeks"
Pick 'F' and place it at the front.
A = "ForGeeksGeeks"
Your Task:  
You dont need to read input or print anything. Complete the function transform() which takes two strings A and B as input parameters and returns the minimum number of steps required to transform A into B. If transformation is not possible return -1.
Expected Time Complexity: O(N) where N is max(length of A, length of B) 
Expected Auxiliary Space: O(1)  
Constraints:
1<= A.length(), B.length() <= 10^{4}
"""

def min_steps_to_transform(A: str, B: str) -> int:
    if len(A) != len(B):
        return -1
    
    # Initialize a list to count character occurrences
    char_count = [0] * 256
    
    # Count characters in A and decrement for characters in B
    for i in range(len(A)):
        char_count[ord(A[i])] += 1
        char_count[ord(B[i])] -= 1
    
    # Check if all counts are zero
    for count in char_count:
        if count != 0:
            return -1
    
    # Calculate the number of operations needed
    i, j = len(A) - 1, len(B) - 1
    operations = 0
    
    while i >= 0:
        if A[i] != B[j]:
            operations += 1
        else:
            j -= 1
        i -= 1
    
    return operations