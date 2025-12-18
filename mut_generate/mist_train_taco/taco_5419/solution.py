"""
QUESTION:
Given string str of a constant length, print a triangle out of it. The triangle should start with the first character of the string and keep growing downwards by adding one character from the string.
The spaces on the left side of the triangle should be replaced with a dot character. 
Example 1:
Input:
str = "geeks"
Output:
....g
...ge
..gee
.geek
geeks
Example 2:
Input:
str = "thisi"
Output:
....t
...th
..thi
.this
thisi
Your Task:  
You don't need to read input. Your task is to complete the function printTriangleDownwards() which takes the string str as an input parameter and prints the required triangle.
Expected Time Complexity: O(N*N), Where N is the size of input string.
Expected Auxiliary Space: O(1)
Constraints:
1 <= |str| <= 500
"""

def generate_triangle_downwards(s: str) -> list[str]:
    N = len(s)
    triangle = []
    for i in range(1, N + 1):
        dots = '.' * (N - i)
        s1 = s[:i]
        triangle.append(dots + s1)
    return triangle