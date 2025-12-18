"""
QUESTION:
Geek is getting really fat. He wants to lose his weight but can't get the motivation to workout. Seeing this, his friend  Heisenberg offers him a deal.
For every K pushups Geek does, Heisenberg will give him money equal to the number of pushups Geek has done till then (Refer Example for Explanation).
Find out the amount of money he made if he does N pushups.
Example 1:
Input: N = 5, K = 2
Output: 6
Explanation: Pushup 1: No Money, Pushup 2: 
+2 Pushup 3: No Money, Pushup 4: +4 and 
Pushup 5: No Money.
Example 2:
Input: N = 5, K = 3
Output: 3
Explanation: Pushup 1: No Money, Pushup 2: 
No Money, Pushup 3: +3, Pushup 4: No Money 
and Pushup 5: No Money.
 
Your Task: 
You don't need to read or print anything. Your task is to complete the function total_Money() which takes N and K as input parameter and returns the amount that Ishan can make.
Expected Time  Complexity: O(1)
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 10^{9}
1 <= K <= 10^{5}
"""

def total_Money(N, K):
    a = N // K
    b = a * K
    return int(a / 2 * (2 * K + (a - 1) * K))