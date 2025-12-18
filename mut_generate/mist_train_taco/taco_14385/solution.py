"""
QUESTION:
Given a string str of lowercase alphabets. The task is to find the maximum occurring character in the string str. If more than one character occurs the maximum number of time then print the lexicographically smaller character.
Example 1:
Input:
str = testsample
Output: e
Explanation: e is the character which
is having the highest frequency.
Example 2:
Input:
str = output
Output: t
Explanation:  t and u are the characters
with the same frequency, but t is
lexicographically smaller.
Your Task:
The task is to complete the function getMaxOccuringChar() which returns the character which is most occurring.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Number of distinct characters).
Note: N = |s|
Constraints:
1 ≤ |s| ≤ 100
"""

def getMaxOccurringChar(s: str) -> str:
    # Convert the string to a set to get unique characters
    unique_chars = list(set(s))
    
    # Initialize a list to store the frequency of each character
    frequencies = [0] * len(unique_chars)
    
    # Count the frequency of each character in the string
    for char in s:
        frequencies[unique_chars.index(char)] += 1
    
    # Find the maximum frequency
    max_freq = max(frequencies)
    
    # Collect all characters that have the maximum frequency
    max_chars = [unique_chars[i] for i in range(len(frequencies)) if frequencies[i] == max_freq]
    
    # Return the lexicographically smallest character among those with the maximum frequency
    return min(max_chars)