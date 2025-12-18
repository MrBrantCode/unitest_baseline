"""
QUESTION:
You are given two integer numbers, the base a and the index b. You have to find the last digit of a^{b}.
 
Example 1:
Input:
a = "3", b = "10"
Output:
9
Explanation:
3^{10} = 59049. Last digit is 9.
Example 2:
Input:
a = "6", b = "2"
Output:
6
Explanation:
6^{2} = 36. Last digit is 6.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function getLastDigit() which takes two strings a,b as parameters and returns an integer denoting the last digit of a^{b}.
 
Expected Time Complexity: O(|b|)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= |a|,|b| <= 1000
Note:|a| = length of a and |b| = length of b. There will not be any test cases such that a^{b }is undefined.
"""

def get_last_digit(a: str, b: str) -> int:
    a = int(a)
    b = int(b)
    
    if a == 0:
        return 0
    if b == 0:
        return 1
    if b == 1:
        return a % 10
    
    d = {
        0: 0,
        1: 1,
        2: [6, 2, 4, 8],
        3: [1, 3, 9, 7],
        4: [6, 4],
        5: 5,
        6: 6,
        7: [1, 7, 9, 3],
        8: [6, 8, 4, 2],
        9: [1, 9]
    }
    
    x = a % 10
    
    if x in [0, 1, 5, 6]:
        return d[x]
    
    if x in [4, 9]:
        y = b % 2
        return d[x][y]
    
    if x in [2, 3, 7, 8]:
        y = b % 4
        return d[x][y]