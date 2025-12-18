"""
QUESTION:
Given a range [m..n]. You task is to find the number of integers divisible by either a or b in the given range. 
 
Example 1:
Input:
m = 5, n = 11, a = 4, b = 6
Output:
2
Explanation:
6 and 8 lie in the range and are also
either divisible by 4 or 6.
Example 2:
Input:
m = 1, n = 3, a = 2, b = 3
Output:
2
Explanation:
2 and 3 lie in the range and are also
either divisible by 2 or 3.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function numOfDiv() which takes 4 Integers m, n, a, b as input and returns the count of integers in the range m..n which are divisible by either a or b.
 
Expected Time Complexity: O(log(max(a,b))
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= m <= n <= 10^{5}
1 <= a,b <= 500
"""

def count_divisibles_in_range(m: int, n: int, a: int, b: int) -> int:
    # Count numbers divisible by a
    count1 = n // a - (m - 1) // a
    
    # Count numbers divisible by b
    count2 = n // b - (m - 1) // b
    
    # Calculate the least common multiple (LCM) of a and b
    c = a * b
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    c //= a
    
    # Count numbers divisible by the LCM of a and b
    count3 = n // c - (m - 1) // c
    
    # Return the total count of numbers divisible by either a or b
    return int(count1 + count2 - count3)