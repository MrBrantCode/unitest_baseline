"""
QUESTION:
Given a sequence of moves for a robot. Check if the sequence is circular or not. 
A sequence of moves is circular if the first and last positions of the robot are the same. A move can be one of the following :
    G - Go one unit
    L - Turn left
    R - Turn right
Example 1:
Input: path = "GLGLGLG"
Output: "Circular"
Explanation: If we start form 
(0,0) in a plane then we will 
back to (0,0) by the end of the 
sequence.
Ã¢â¬â¹Example 2:
Input: path = "GGGGL"
Output: "Not Circular"
Explanation: We can't return to 
same place at the end of the path.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function isCircular() which takes the string path as input and returns "Circular" if the path is circular else returns "Not Circular".
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |S| ≤ 10^{5}
"""

def is_circular(path: str) -> str:
    i = j = 0
    pre = 'r'
    for k in path:
        if k == 'G':
            if pre == 'r':
                j += 1
            elif pre == 'l':
                j -= 1
            elif pre == 'u':
                i -= 1
            elif pre == 'd':
                i += 1
        elif k == 'L':
            if pre == 'r':
                pre = 'u'
            elif pre == 'l':
                pre = 'd'
            elif pre == 'u':
                pre = 'l'
            elif pre == 'd':
                pre = 'r'
        elif k == 'R':
            if pre == 'r':
                pre = 'd'
            elif pre == 'l':
                pre = 'u'
            elif pre == 'u':
                pre = 'r'
            elif pre == 'd':
                pre = 'l'
    if i == 0 and j == 0:
        return 'Circular'
    return 'Not Circular'