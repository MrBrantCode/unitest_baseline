"""
QUESTION:
Using seven segment display, you can write down any digit from 0 to 9 using at most seven segments. Given a positive number N and then a string S representing a number of N digits. You have to rearrange the segments in this N digit number to get the smallest possible N digit number. This number can have leading zeros. You can not waste any segment or add any segment from your own. You have to use all of the segments of the given N digits. 
Note: You can refer this diagram for more details
Example 1:
Input:
N = 6
S = "234567"
Output:
000011
Explanation:
234567 has a total of 28 segments and
we can rearrange them to form 000011
which has 28 segments too. 000011 is the
smallest possible number which can be
formed on rearrangement.
Example 2:
Input:
N = 3
S = "011"
Output:
011
Explanation:
011 has a total of 10 segments and this
is the smallest number with 10 segments.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function sevenSegments() which takes an Integer N and a String S of length N as input and returns the smallest possible N digit number which can be made using all of the segments given.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{4}
"""

def smallest_seven_segment_number(N, S):
    segs = [6, 2, 5, 5, 4, 5, 6, 3, 7, 5]
    total = sum((segs[int(S[i])] for i in range(N)))
    ans = ['0'] * N
    
    for i in range(N):
        if total == 2 * (N - i):
            ans[i] = '1'
            total -= 2
        elif total == 7 * (N - i):
            ans[i] = '8'
            total -= 7
        elif total - 6 >= 2 * (N - i - 1) and total - 6 <= 7 * (N - i - 1):
            ans[i] = '0'
            total -= 6
        elif total - 2 <= 7 * (N - i - 1):
            ans[i] = '1'
            total -= 2
        elif total - 3 <= 7 * (N - i - 1):
            ans[i] = '7'
            total -= 3
        elif total - 4 <= 7 * (N - i - 1):
            ans[i] = '4'
            total -= 4
        elif total - 5 <= 7 * (N - i - 1):
            total -= 5
            ans[i] = '2'
    
    return ''.join(ans)