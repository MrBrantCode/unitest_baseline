"""
QUESTION:
Adobe wants to play a game. He is given a number N. He has to create a alphabetical string in lower case from that number and tell whether the string is palindrome or not. a = 0 , b = 1….. and so on.  For eg : If the number is 61 the substring “gb” will be printed till 7 (6+1) characters i.e. “gbgbgbg” and check if palindrome or not. Adobe is weak in concepts of palindrome and strings, help him in winning the game.
Note: No number will start with zero. Consider alphabets ' a to j ' only i.e. single digit numbers from 0 to 9.
Example 1:
Ã¢â¬â¹Input : N = 61
Output : YES
Explanation:
N = 61 the substring “gb” will be 
printed till 7 (6+1) characters i.e. 
“gbgbgbg” and it is palindrome. return 
true.
Ã¢â¬â¹Example 2:
Input : N = 1998 
Output :  NO 
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function pallan() that takes an integer (N), and return true if the string is a palindrome otherwise return false if not. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
1 ≤ N ≤ 10^{7}
"""

def is_pallan_palindrome(n: int) -> bool:
    # Mapping of digits to corresponding alphabets
    digit_to_alpha = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j'}
    
    # Convert the number to a string
    s = str(n)
    
    # Generate the alphabetical string from the digits
    s1 = ''.join(digit_to_alpha[int(digit)] for digit in s)
    
    # Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in s)
    
    # Determine the length of the final string
    repeat_count = digit_sum // len(s)
    remainder = digit_sum % len(s)
    
    # Construct the final string
    if remainder == 0:
        final_str = s1 * repeat_count
    else:
        final_str = (s1 * repeat_count) + s1[:remainder]
    
    # Check if the final string is a palindrome
    return final_str == final_str[::-1]