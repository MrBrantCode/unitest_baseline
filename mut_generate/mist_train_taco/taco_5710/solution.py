"""
QUESTION:
Shil is your new boss and he likes palindromes very much.  Palindrome is a string that can be read the same way in either direction, from the left to the right and from the right to the left. (ex. madam , aabaa, racecar)  

Given a string S , beautiful Palindrome is a lexicographical minimum palindrome that can be formed by rearranging all the characters of string S. In order to please your boss, find a beautiful Palindrome that can be formed with help of string S.  

String x is lexicographically less than string y, if either x is a prefix of y (and x ≠ y), or there exists such i (1 ≤ i ≤ min(|x|, |y|)), that xi < yi, and for any j (1 ≤ j < i) xj = yj. Here |a| denotes the length of the string a. The lexicographic comparison of strings is implemented by operator < in modern programming languages​​.

Input:
Only line of input contains string S. All the letters of this string will be in lower letters('a' - 'z').

Output:
Output lexicographical minimum Palindrome that can be formed by rearranging all the letters of string S. If no such Palindrome exist for given  input, print -1.

Constraints: 
1≤|S|≤100000

SAMPLE INPUT
aabcc

SAMPLE OUTPUT
acbca

Explanation

After rearranging all the characters , all the palindromes that can be formed are cabac and acbca. Out of these two lexicographical minimum one is acbca.
"""

def find_lexicographical_minimum_palindrome(s: str) -> str:
    # Create a list of all lowercase letters
    alphabet = [chr(i + ord('a')) for i in range(26)]
    
    # Initialize a frequency dictionary for each letter
    f = dict(zip(alphabet, [0] * 26))
    
    # Count the frequency of each character in the input string
    for c in s:
        f[c] += 1
    
    # Initialize the output string
    output = ''
    
    # Construct the left half of the palindrome
    for c in alphabet:
        while f[c] > 1:
            output += c
            f[c] -= 2
    
    # Collect characters that can be placed in the middle
    mid = []
    for k, v in f.items():
        if v == 1:
            mid.append(k)
    
    # If there is more than one character with an odd frequency, return -1
    if len(mid) > 1:
        return '-1'
    
    # Construct the final palindrome
    return output + ''.join(mid) + output[::-1]