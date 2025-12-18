"""
QUESTION:
Given a one/two-digit timing, calculate the possibilities of occurrence of other timings(including the glowing one) with relevant to glowing segments, assuming some segments may not be glowing.
Displaying the numbers is done using a seven-segment display. It is guaranteed that the sticks currently displaying are working fine.
Example 1:
Input:
S = "78"
Output:
5
Explanation:
7 can be replaced by 
5 different numbers 
9, 3, 8, 0, and 7
(if none of the segment 
is broken) and 8 can be 
replaced by only 1 
number i.e 8 itself
(if none of the the 
segment is broken), 
therefore the answer 
is 5*1=5.
 
 
Example 2:
Input:
S = "05"
Output:
8
Explanation:
0 can be replaced by 
2 numbers, 8 and 0,
while 5 can be replaced
by 4 different numbers.
So, the answer is 4*2=8.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function numberOfPossibleTimings() which takes a string S and return number of possible timings.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
 
Constraints:
0<=x<=99
Note:  The number x should contain 2 digits like 1 should be written as 01.
"""

def numberOfPossibleTimings(S: str) -> int:
    # Array representing the number of possible replacements for each digit (0-9)
    a = [2, 7, 2, 3, 3, 4, 2, 5, 1, 2]
    
    # Extract the number of possible replacements for the first and second digits
    x = a[int(S[0])]
    y = a[int(S[1])]
    
    # Return the product of the possible replacements for the two digits
    return x * y