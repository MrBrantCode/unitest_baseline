"""
QUESTION:
Given a number num, our task is to find the closest Palindrome number whose absolute difference with given number is minimum. If 2 Palindome numbers have same absolute difference from the given number, then find the smaller one.
 
Example 1:
Input: num = 9
Output: 9
Explanation: 9 itself is a palindrome
number.
Example 2:
Input: num = 489
Output: 484
Expnataion: closest palindrome numbers from
489 are 484 and 494. Absolute difference between
489 and 494 is equal to the absolute difference
between 484 and 489 but 484 is smaller than 494.
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function closestPalindrome() which takes num as input parameter and returns the closest palindrome.
 
Expected Time Complexity: O(log_{10}num)
Expected Space Complexity: O(1)
 
Constraints:
1 <= num <= 10^{14}
"""

import math

def find_closest_palindrome(num: int) -> int:
    if num < 10:
        return num
    elif math.log10(num) % 1 == 0:
        return num - 1
    else:
        str_num = str(num)
        half_len = (len(str_num) + 1) // 2
        first_half = str_num[:half_len]
        
        if len(str_num) % 2 == 0:
            n1 = int(first_half + first_half[::-1])
            n2 = int(str(int(first_half) + 1) + str(int(first_half) + 1)[::-1])
            n3 = int(str(int(first_half) - 1) + str(int(first_half) - 1)[::-1])
        else:
            n1 = int(first_half[:-1] + first_half[::-1])
            n2 = int(str(int(first_half) + 1)[:-1] + str(int(first_half) + 1)[::-1])
            n3 = int(str(int(first_half) - 1)[:-1] + str(int(first_half) - 1)[::-1])
        
        if abs(num - n3) <= abs(num - n1) and abs(num - n3) <= abs(num - n2):
            return n3
        elif abs(num - n1) <= abs(num - n2):
            return n1
        else:
            return n2