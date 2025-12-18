"""
QUESTION:
There are infinite number of cities in Geekland numbered from 1 onward. Some of them are connected via bidirectional railway tracks.
There are railway tracks 1-2, 3-4, 5-6, 7-8, and so on.
There are railway tracks between every two consecutive odd numbers. 1-3, 3-5, 5-7, 7-9, and so on.
There are railway tracks between every two consecutive even numbers. 2-4, 4-6, 6-8, 8-10, and so on.
Given two cities a and b, check if there is a railway track between them or not.
Example 1:
Input: 
a = 1, b = 4
Output: NO
Explaination: There is no direct track 
between 1 and 4.
Example 2:
Input: 
a = 4, b = 3
Output: YES
Explaination: There is a direct track 
between 3 and 4.
Your Task:
You do not need to read input or print anything. Your task is to complete the function isConnected() which takes a and b as input parameters and returns 1 if there is a direct connection, otherwise, returns 0.
Note: The generated output is YES when you return 1 and NO when you return 0.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ a, b ≤ 10^{9}
"""

def is_connected(a: int, b: int) -> int:
    if a % 2 == 0:
        if b == a + 2 or b == a - 1 or b == a - 2:
            return 1
        else:
            return 0
    elif a % 2 != 0:
        if b == a + 1 or b == a + 2 or b == a - 2:
            return 1
        else:
            return 0
    else:
        return 0