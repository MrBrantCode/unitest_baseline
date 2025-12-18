"""
QUESTION:
Given a word pat and a text txt. Return the count of the occurrences of anagrams of the word in the text.
Example 1:
Input:
txt = forxxorfxdofr
pat = for
Output: 3
Explanation: for, orf and ofr appears
in the txt, hence answer is 3.
Example 2:
Input:
txt = aabaabaa
pat = aaba
Output: 4
Explanation: aaba is present 4 times
in txt.
Your Task:
Complete the function search() which takes two strings pat, txt, as input parameters and returns an integer denoting the answer. 
You don't need to print answer or take inputs.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(26) or O(256)
Constraints:
1 <= |pat| <= |txt| <= 10^{5}
Both strings contain lowercase English letters.
"""

def count_anagram_occurrences(txt: str, pat: str) -> int:
    k = len(pat)
    d_pat = {}
    
    # Create a frequency dictionary for the pattern
    for char in pat:
        d_pat[char] = d_pat.get(char, 0) + 1
    
    d_txt = {}
    n = len(txt)
    (i, j) = (0, 0)
    count = 0
    
    while j < n:
        # Add the current character to the frequency dictionary of the text window
        d_txt[txt[j]] = d_txt.get(txt[j], 0) + 1
        
        # When the window size is equal to the pattern length
        if j - i + 1 == k:
            # Check if the current window matches the pattern's frequency dictionary
            if d_pat == d_txt:
                count += 1
            
            # Slide the window by removing the leftmost character
            d_txt[txt[i]] -= 1
            if d_txt[txt[i]] == 0:
                del d_txt[txt[i]]
            i += 1
        
        j += 1
    
    return count