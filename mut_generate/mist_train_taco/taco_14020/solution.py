"""
QUESTION:
Joey is a food lover, but Monica is concerned about his health and thus refuses to give him any more food. But on Joey's request, she agrees to give him more food only if he solves this problem. You have two integers a and b which are the number of C's and the number of S's. You need to find the maximum number of words of "SCC" which can be formed from this.
Note:  2 C's can form a S.
Example 1:
Input:
a = 2 
b = 1
Output:
1
Explanation:
We have a = 2 which means we have 2 C's and b = 1
which means we have a S.
therefore we can make only 1 "SCC".
Example 2:
Input:
a = 3 
b = 1
Output:
1
Explanation:
We have a = 3 which means we have 3 C's and b = 1
which means we have a S.
therefore we can make only 1 "SCC". and 1 C is
remaining which cannot be used to form more "SCC".
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countSCC() which takes two integers a and b as input parameter and returns the count of "SCC" formed using a number of C and b number of S.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1 <= a,b <= 10^{8}
"""

def countSCC(a: int, b: int) -> int:
    if a == 2 * b:
        return b
    elif 2 * b > a:
        return a // 2
    else:
        c_left = a - 2 * b
        c_left_s = c_left // 4
        return b + c_left_s