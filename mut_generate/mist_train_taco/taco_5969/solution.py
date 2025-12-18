"""
QUESTION:
Given N dots that form a triangle such that i^{th }line contains i number of dots.
    .
   . .
  . . .
 . . . .
Find the minimum hieght H of the triangle that can be formed using these N dots.
 
Example 1:
Input: N = 2
Output: 1
Explaination: The height will be 1. We 
need one dot to create first line. With 
the remaining one dot we cannot complete the 
second line.
 
Example 2:
Input: N = 10
Output: 4
Explaination: With 10 dots we can complete 
total four lines. The layers will have 1, 
2, 3 and 4 dots respectively.
 
Your Task:
You do not need to read input or print anything. Your task is to complete the function height() which takes N as input parameter and returns the height of the triangle that we can form using N dots.
 
Expected Time Comlpexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 ≤ N ≤ 10^{5}
"""

def calculate_triangle_height(N: int) -> int:
    count = 1
    height = 1
    i = 1
    while count <= N:
        count += i + 1
        i += 1
        height += 1
    return height - 1