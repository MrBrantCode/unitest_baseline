"""
QUESTION:
Given binary string str consisting of only 0's and 1's, Check if all the 0's are together or not.
Example 1:
Input:
str = "000"
Output:
YES
Explanation:
All the 0's are together.
Example 2:
Input:
str = "111"
Output:
NO
Explanation:
All the 0's are not together.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function checkTogether() which takes the binary string str as an input parameter and returns 1 if all the 0's are together else returns 0.
Expected Time Complexity: O(N), Where N is the size of the string.
Expected Auxiliary Space: O(1)
Constraints:
1 <= |str| <= 10000
"""

def are_zeros_together(str):
    temp = False
    for i in range(len(str)):
        if str[i] == '0' and (not temp):
            temp = True
        elif str[i] == '1' and temp == True:
            z = str[i:len(str)]
            if '0' in z:
                temp = False
                break
    return temp