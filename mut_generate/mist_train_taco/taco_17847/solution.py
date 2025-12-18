"""
QUESTION:
Given a string S of lowercase english alphabetic characters and a substring range starting from q1 and ending at q2, the task is to find out the count of palindromic substrings in the given substring range.
Example 1:
Input:
N = 7 
S = "xyaabax"
q1 = 3
q2 = 5
Output: 4
Explanation: The substring in the given range 
is "aba". Hence, the palindromic substrings are:
"a", "b", "a" and "aba".
Ã¢â¬â¹Example 2:
Input: 
N = 7
S = "xyaabax" 
q1 = 2 
q2 = 3. 
Output: 3
Explanation: The substring in the given range
is "aa". Hence, the palindromic substrings are: 
"a", "a" and "aa".
Your Task:
You don't need to read input or print anything. Your task is to complete the function countPalinInRange() which takes the string S, its length N and the range variables q1 and q2 as input parameters and returns the count of the Palindromic substrings in the given substring range.
Expected Time Complexity: O(|S|^{2}).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ |S| ≤ 1000
0 ≤ q1, q2 < |S|
"""

def count_palindromic_substrings_in_range(S: str, q1: int, q2: int) -> int:
    res = 0
    
    # Ensure q1 is less than or equal to q2
    if q1 > q2:
        q1, q2 = q2, q1
    
    # Iterate over the substring range
    for i in range(q1, q2 + 1):
        # Count odd length palindromes centered at i
        j = i - 1
        k = i + 1
        res += 1  # Single character is always a palindrome
        while j >= q1 and k <= q2:
            if S[j] == S[k]:
                res += 1
            else:
                break
            j -= 1
            k += 1
        
        # Count even length palindromes centered between i and i+1
        if i < len(S) - 1 and S[i] == S[i + 1]:
            j = i
            k = i + 1
            while j >= q1 and k <= q2:
                if S[j] == S[k]:
                    res += 1
                else:
                    break
                j -= 1
                k += 1
    
    return res