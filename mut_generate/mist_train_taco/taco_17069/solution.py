"""
QUESTION:
Given a positive number X. Find the largest Jumping Number which is smaller than or equal to X. 
Jumping Number: A number is called Jumping Number if all adjacent digits in it differ by only 1. All single-digit numbers are considered as Jumping Numbers. For example 7, 8987 and 4343456 are Jumping numbers but 796, 677 and 89098 are not.
 
Example 1:
Input:
X = 10
Output:
10
Explanation:
10 is the largest Jumping Number
possible for X = 10.
Example 2:
Input:
X = 50
Output:
45
Explanation:
45 is the largest Jumping Number
possible for X = 50.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function jumpingNums() which takes an Integer X as input and returns the largest Jumping Number less than or equal to X.
 
Expected Time Complexity:  O(k), where k is no of jumping numbers
Expected Auxiliary Space: O(k), where k is no of jumping numbers 
 
Constraints:
1 <= X <= 10^{9}
"""

from collections import deque

def find_largest_jumping_number(X: int) -> int:
    def generate_all_jumping_nums(X, i):
        J = deque()
        J.append(i)
        while J:
            num = J.popleft()
            if num <= X:
                nonlocal ans
                ans = max(ans, num)
                last_dig = num % 10
                if last_dig != 9:
                    J.append(num * 10 + last_dig + 1)
                if last_dig != 0:
                    J.append(num * 10 + last_dig - 1)

    ans = 0
    for i in range(1, 10):
        if i <= X:
            generate_all_jumping_nums(X, i)
    return ans