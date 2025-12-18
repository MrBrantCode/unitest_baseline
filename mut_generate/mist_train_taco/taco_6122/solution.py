"""
QUESTION:
Given a string S and an array roll where roll[i] represents rolling first roll[i] characters in the string, the task is to apply every roll[i] on the string and output the final string. Rolling means increasing the ASCII value of character, like rolling z would result in a, rolling b would result in c, etc.
 
Example 1:
Input: s = "bca"
roll[] = {1, 2, 3} 
Output: eeb
Explanation: arr[0] = 1 means roll 
first character of string -> cca
arr[1] = 2 means roll 
first two characters of string -> dda
arr[2] = 3 means roll
first three characters of string -> eeb
So final ans is "eeb".
 
Example 2:
Input: s = "zcza"
roll[] = {1, 1, 3, 4}
Output: debb
 
Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function findRollOut() that takes String S, array roll, and integer N as parameters and returns the modified string.
Note- The length of the array roll and length of the string are equal.
 
Expected Time Complexity: O(N). 
Expected Auxiliary Space: O(N).
 
Constraints:
1 ≤ N ≤ 10^{7}
"""

def apply_rolls(s: str, roll: list[int]) -> str:
    n = len(s)
    freq = [0] * (n + 2)
    
    # Calculate the frequency of rolls for each position
    for index in range(n):
        freq[roll[index]] += 1
    
    # Accumulate the frequency from the end to the start
    for index in range(n, -1, -1):
        freq[index] += freq[index + 1]
        freq[index] %= 26
    
    # Apply the rolls to the string
    res = ''
    for index in range(n):
        final_val = ord(s[index]) + freq[index + 1]
        final_val = final_val if 97 <= final_val <= 122 else final_val - 26
        res += chr(final_val)
    
    return res