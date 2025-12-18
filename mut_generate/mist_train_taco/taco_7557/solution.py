"""
QUESTION:
Given two strings A and B. Find the characters that are not common in the two strings. 
Note :- Return the string in sorted order.
Example 1:
Input:
A = geeksforgeeks
B = geeksquiz
Output: fioqruz
Explanation: 
The characters 'f', 'i', 'o', 'q', 'r', 'u','z' 
are either present in A or B, but not in both.
Example 2:
Input:
A = characters
B = alphabets
Output: bclpr
Explanation: The characters 'b','c','l','p','r' 
are either present in A or B, but not in both.
Your Task:  
You dont need to read input or print anything. Complete the function UncommonChars() which takes strings A and B as input parameters and returns a string that contains all the uncommon characters in sorted order. If no such character exists return "-1".
Expected Time Complexity: O(M+N) where M and N are the sizes of A and B respectively.
Expected Auxiliary Space: O(M+N)  
Constraints:
1<= M,N <= 10^{4}
String may contain duplicate characters.
"""

def find_uncommon_characters(A: str, B: str) -> str:
    set_a = set(A)
    set_b = set(B)
    uncommon_in_a = set_a - set_b
    uncommon_in_b = set_b - set_a
    
    if not uncommon_in_a and not uncommon_in_b:
        return "-1"
    
    uncommon_chars = sorted(uncommon_in_a.union(uncommon_in_b))
    return ''.join(uncommon_chars)