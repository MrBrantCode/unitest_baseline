"""
QUESTION:
Given a string S. Count the characters that have ‘N’ number of occurrences. If a character appears consecutively it is counted as 1 occurrence.
Example 1:
Input:
S = "abc", N = 1
Output: 3
Explanation: 'a', 'b' and 'c' all have 
1 occurrence.
Ã¢â¬â¹Example 2:
Input: 
S = "geeksforgeeks", N = 2
Output: 4
Explanation: 'g', 'e', 'k' and 's' have
2 occurrences.
Your Task:
You don't need to read input or print anything. Your task is to complete the function getCount() which takes the string S and an integer N as inputs and returns the count of the characters that have exactly N occurrences in the string. Note that the consecutive occurrences of a character have to be counted as 1.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).
Constraints:
1<=|S|<=10^{5}
1<=N<=10^{3}
"""

def count_characters_with_n_occurrences(S: str, N: int) -> int:
    # Remove consecutive duplicates
    i = 1
    while i < len(S) - 1:
        if S[i] == S[i - 1]:
            S = S[:i] + S[i + 1:]
            i -= 1
        if S[i] == S[i + 1]:
            S = S[:i + 1] + S[i + 2:]
            i -= 1
        i += 1
    
    # Count occurrences of each character
    my_dict = {}
    for char in S:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    
    # Count characters with exactly N occurrences
    count = 0
    for occurrences in my_dict.values():
        if occurrences == N:
            count += 1
    
    return count