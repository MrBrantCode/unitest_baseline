"""
QUESTION:
Count the numbers between 1 to N containing 4 as a digit.
 
Example 1:
Input:
N = 9
Output:
1
Explanation:
4 is the only number between 1 to 9
which contains 4 as a digit.
Example 2:
Input:
N = 14
Output:
2
Explanation:
4 and 14 are the only number between 1
to 14 that contains 4 as a digit.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function countNumberswith4() which takes an Integer N as input and returns the answer.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
"""

def count_numbers_with_4(N: int) -> int:
    def contains_4(x: int) -> bool:
        while x:
            if x % 10 == 4:
                return True
            x //= 10
        return False

    count = 0
    for i in range(1, N + 1):
        if contains_4(i):
            count += 1
    return count