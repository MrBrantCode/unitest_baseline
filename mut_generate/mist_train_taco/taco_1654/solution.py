"""
QUESTION:
You are given the sequence: 0123456789101112131415...
The 0th digit of this sequence is 0, the 1st digit of this sequence is 1, the 2nd digit of this sequence is 2 and so on. You are given n, find the nth digit of the sequence.
 
Example 1:
Input: n = 12
Output: 1
Explanation: 1 is the 12th digit of the
given sequence.
Example 2:
Input: n = 20
Output: 4
Explanation: 4 is the 20th digit of the
given sequence.
 
Your Task:
You don't need to read or write anything. Your task is to complete the function NthDigit() which takes n as input parameter and returns the nth digit of the sequence.
 
Expected Time Complexity: O(log_{10}(n))
Expected Space Compelxity: O(1)
 
Constraints:
1 <= n <= 10^{9}
"""

def find_nth_digit(n: int) -> int:
    cnt, r = 0, 1
    while True:
        cnt += r * pow(10, r - 1) * 9
        if cnt >= n:
            break
        r += 1
    cnt -= r * pow(10, r - 1) * 9
    n -= cnt
    q, rem = divmod(n, r)
    num = q + pow(10, r - 1) - 1
    if rem == 0:
        return num % 10
    else:
        num += 1
        ans = str(num)
        return int(ans[rem - 1])