"""
QUESTION:
Convert a given string to its cross string (i.e Diagonal from left-right and from right-left).  
See examples for better understanding.
 
Example 1:
Input:
abc
Output:
a c  b  a c
Explanation:
The above is the proper 
cross manner for the 
test case.
a c
 b 
a c
Example 2:
Input:
geeks
Output:
g   s e k   e   e k g   s
Explanation:
For the 1st test case where 
the string is geeks
G   S
 E K
  E
 E K
G   S
The above is the proper cross 
the manner for the test case, but 
when printed in a single line 
it becomes as shown in the output.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function crossPattern() which takes the string S and returns a single string in the following way first-line output of the string concatenated with 2nd line and so on till the Nth line.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 ≤ length of string ≤ 1000
"""

def generate_cross_pattern(S: str) -> str:
    start = ''
    end = ''
    n = len(S)
    
    for i in range(n // 2):
        row = i * ' ' + S[i] + (n - 2 * (i + 1)) * ' ' + S[-i - 1] + i * ' '
        start += row
        end = row + end
    
    if n % 2:
        start += n // 2 * ' ' + S[n // 2] + n // 2 * ' '
    
    return start + end