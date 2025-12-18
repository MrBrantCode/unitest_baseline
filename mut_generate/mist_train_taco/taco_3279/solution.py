"""
QUESTION:
Rahul and Ankit are the only two waiters in the Royal Restaurant. Today, the restaurant received n orders. The amount of tips may differ when handled by different waiters, if Rahul takes the i_{th} order, he would be tipped a_{i} rupees and if Ankit takes this order, the tip would be b_{i} rupees.
In order to maximize the total tip value they decided to distribute the order among themselves. One order will be handled by one person only. Also, due to time constraints Rahul cannot take more than x orders and Ankit cannot take more than y orders. It is guaranteed that x + y is greater than or equal to n, which means that all the orders can be handled by either Rahul or Ankit. Find out the maximum possible amount of total tip money after processing all the orders.
Example 1:
Input:
n = 5, x = 3, y = 3
a[] = {1, 2, 3, 4, 5}
b[] = {5, 4, 3, 2, 1}
Output: 21
Explanation: Rahul will serve 3rd, 4th 
and 5th order while Ankit will serve 
the rest.
Example 2:
Input:
n = 8, x = 4, y = 4
a[] = {1, 4, 3, 2, 7, 5, 9, 6}
b[] = {1, 2, 3, 6, 5, 4, 9, 8}
Output: 43
Explanation: Rahul will serve 1st, 2nd, 5th 
and 6th order while Ankit will serve the rest.
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxTip() which takes array a[ ], array b[ ], n, x and y as input parameters and returns an integer denoting the answer.
Expected Time Complexity: O(n*logn)
Expected Auxiliary Space: O(n)
Constraints:
1 ≤ n ≤ 10^{5}
1 ≤ x, y ≤ N
x + y ≥ n
1 ≤ a[i], b[i] ≤ 10^{5}
"""

def max_tip(a, b, n, x, y):
    mx = 0
    diff_contribution = [abs(a[index] - b[index]) for index in range(n)]
    diff_contribution = sorted(enumerate(diff_contribution), key=lambda d: -d[1])
    diff_index = [d[0] for d in diff_contribution]
    for index_value in diff_index:
        if a[index_value] >= b[index_value] and x:
            mx += a[index_value]
            x -= 1
        elif a[index_value] < b[index_value] and y:
            mx += b[index_value]
            y -= 1
        elif not x and y:
            mx += b[index_value]
            y -= 1
        elif not y and x:
            mx += a[index_value]
            x -= 1
    return mx