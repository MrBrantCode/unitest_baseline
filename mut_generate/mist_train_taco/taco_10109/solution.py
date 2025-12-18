"""
QUESTION:
Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first ( with the least starting index ).
Example 1:
Input:
S = "aaaabbaa"
Output:
aabbaa
Explanation:
The longest palindrome string present in
the given string is "aabbaa".
Your Task:  
You don't need to read input or print anything. Your task is to complete the function longestPalindrome() which takes string S as input parameters and returns longest pallindrome present in string.
Expected Time Complexity: O(|S|^{2})
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |S| ≤ 10^{4}
"""

def find_longest_palindrome(S: str) -> str:
    # Initialize the longest palindrome to be the first character of the string
    longest_palindrome = S[0]
    
    # Iterate over each possible starting index of the substring
    for i in range(len(S)):
        # Iterate over each possible ending index of the substring
        for j in range(i + 1, len(S) + 1):
            # Extract the substring from index i to j
            substring = S[i:j]
            # Check if the substring is a palindrome and longer than the current longest palindrome
            if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                # Update the longest palindrome
                longest_palindrome = substring
    
    # Return the longest palindromic substring found
    return longest_palindrome