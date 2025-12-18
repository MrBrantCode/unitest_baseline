"""
QUESTION:
Consider a series of numbers composed of only digits 4 and 7. First few numbers in the series are 4, 7, 44, 47, 74, 77, 444, .. etc. Given a string N constructed by 4, 7 digit only, find position of this number in this series.
 
Example 1:
Input: N = "7"
Output: 2
Explanation: In the series 4 , 7 , 44 , 47...
7 is at second position.
 
Example 2:
Input: N = "444"
Output: 7
Explanation: In the series 4 , 7 , 44 ,
47 , 74 , 77 , 444 , 447... 444 is at 7th
position 
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function findpos() which accepts a string N as input parameter and returns the position of that string in the given series.
 
Expected Time Complexity: O(Length of given string)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= Length of String < 50
"""

def find_position_in_series(n: str) -> int:
    cnt = [0] * 51
    for i in range(1, 51):
        cnt[i] = 2 ** i
    total = cnt.copy()
    for i in range(1, 51):
        total[i] += total[i - 1]
    sz = len(n)
    ans = total[sz - 1]
    for i in range(sz - 1):
        if n[i] == '7':
            ans += cnt[sz - 1 - i]
    ans += 1 if n[-1] == '4' else 2
    return ans