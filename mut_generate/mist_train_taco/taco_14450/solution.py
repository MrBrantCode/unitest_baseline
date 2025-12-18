"""
QUESTION:
Given a large positive number N having x digits, the task is to count all rotations of the given number which are divisible by 4.
Example 1:
Input: N = 8
Output: 1
Explaination: The number 8 is divisible by 4.
Example 2:
Input: N = 20
Output: 1
Explaination: The number 20 is divisible by 4. 
But after rotation 02 is not divisible by 4.
Your Task:
You do not need to read input or print anything. Your task is to complete the function countRotations() which takes N as input parameter and returns the number of rotations divisible by 4.
Expected Time Complexity: O(x)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ x ≤ 10^{5}
"""

def count_divisible_rotations(N: int) -> int:
    s = str(N)
    count = 0
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        if int(rotated) % 4 == 0:
            count += 1
    return count