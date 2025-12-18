"""
QUESTION:
Given a string str containing alphanumeric characters. The task is to calculate the sum of all the numbers present in the string.
Example 1:
Input:
str = 1abc23
Output: 24
Explanation: 1 and 23 are numbers in the
string which is added to get the sum as
24.
Example 2:
Input:
str = geeks4geeks
Output: 4
Explanation: 4 is the only number, so the
sum is 4.
Your Task:
The task is to complete the function findSum() which finds and returns the sum of numbers in the string.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 <= length of the string <= 10^{5}
Sum of Numbers <= 10^{5}
"""

def calculate_sum_of_numbers_in_string(s: str) -> int:
    temp = 0
    ans = 0
    for item in s:
        if item.isdigit():
            if temp == 0:
                temp = int(item)
            else:
                temp = 10 * temp + int(item)
        else:
            ans += temp
            temp = 0
    ans += temp
    return ans