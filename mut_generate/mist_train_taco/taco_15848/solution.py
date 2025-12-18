"""
QUESTION:
For a given string S, comprising of only lowercase English alphabets, eliminate the vowels from the string that occur between two consonants(sandwiched between two immediately adjacent consonants). Print the updated string on a new line.
Example 1:
Input : S = "bab"
Output : bb
Explanation:
a is a vowel occuring between two consonants i.e. b. 
Hence the updated string eliminates a.
Example 2:
Input : S = "ceghij"
Output : cghj
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function Sandwiched_Vowel() that takes a String (s), and return the updated String. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ L ≤ 10^{5}, where L is length of string S
'a' ≤ S[i] ≤ 'z', i is an integer denoting index of S
"""

def remove_sandwiched_vowels(s: str) -> str:
    vowels = 'aeiou'
    updated_string = ''
    n = len(s)
    
    for i in range(n):
        if s[i] in vowels:
            if i > 0 and i < n - 1 and (s[i - 1] not in vowels) and (s[i + 1] not in vowels):
                continue
        updated_string += s[i]
    
    return updated_string