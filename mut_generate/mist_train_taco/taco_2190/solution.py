"""
QUESTION:
Jack is very fond of reading. He reads a lot many pages of books in a day. Since he is obsessed with reading, he reads K times more pages than the number of pages he read the previous day.He read 1 page on the first day. He wants to see that on any given day N, how many pages will he read.Since the answer can be very large, find the answer in modulo 10^{9}+7.
Example 1:
Input: N = 5, K = 2 
Output: 16 
Explanation: 
On Day 1 : 1
On Day 2 : 2
On Day 3 : 4
On Day 4 : 8
On Day 5 : 16
So the answer is 16. 
Example 2:
Input: N = 2, K = 3 
Output: 3
Explanation: 
On Day 1 : 1
On Day 2 : 3
So the answer is 3. 
Your Task:  
You dont need to read input or print anything. Complete the function nthDayPage() which takes N and K as input parameter and returns the answer.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1<= N <=10^{6}
1<= K <=10^{3}
"""

def calculate_pages_on_nth_day(N: int, K: int) -> int:
    MODULO = 1000000007
    N = N - 1
    x = K ** N
    x = x % MODULO
    return x