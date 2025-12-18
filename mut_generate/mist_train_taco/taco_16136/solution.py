"""
QUESTION:
Arya has a string, s, of uppercase English letters. She writes down the string s on a paper k times. She wants to calculate the occurence of a specific letter  in the first n characters of the final string.
Example
Input : 
s = "ABA"
k = 3
n = 7
c = 'B'
Output : 
2
Explaination : 
Final string - ABAABAABA
Example 
Input : 
s = "MMM"
k = 2
n = 4
c = 'M'
Output :
4
Explaination : 
Final string - MMMMMM
Ã¢â¬â¹Your Task:
You don't need to read input or print anything. Your task is to complete the function fun() which takes the string s , integer k ,integer n and the character c as input parameter and returns the occurence of the character c  in the first n characters of the final string.
Expected Time Complexity : O(|s|)
Expected Auxiliary Space : O(1)
Constraints:
1 <= |s| <= 10^{5}
1 <= k <= 10^{5}
1 <= n <= |s|*k
"""

def count_character_in_final_string(s: str, k: int, n: int, c: str) -> int:
    # Calculate the length of the original string
    len_s = len(s)
    
    # Calculate the number of complete repetitions of s within the first n characters
    full_reps = n // len_s
    
    # Calculate the number of characters in the partial repetition at the end
    partial_len = n % len_s
    
    # Count the occurrences of c in one complete repetition of s
    count_in_full_rep = s.count(c)
    
    # Count the occurrences of c in the partial repetition
    count_in_partial_rep = s[:partial_len].count(c)
    
    # Total occurrences in the first n characters
    total_count = (count_in_full_rep * full_reps) + count_in_partial_rep
    
    return total_count