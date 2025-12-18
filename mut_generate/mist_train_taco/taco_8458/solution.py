"""
QUESTION:
Given a string text, we are allowed to swap two of the characters in the string. Find the length of the longest substring with repeated characters.
 
Example 1:
Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa", which its length is 3.

Example 2:
Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa", which its length is 6.

Example 3:
Input: text = "aaabbaaa"
Output: 4

Example 4:
Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa", length is 5.

Example 5:
Input: text = "abcdef"
Output: 1

 
Constraints:

1 <= text.length <= 20000
text consist of lowercase English characters only.
"""

def max_length_of_repeated_substring(text: str) -> int:
    letters = {}
    for (i, char) in enumerate(text):
        if char in letters:
            letters[char].append(i)
        else:
            letters[char] = [i]
    
    if len(letters) == 1:
        return len(text)
    
    ans = 0
    for letter in letters:
        cur = 0
        prev = 0
        discarded = False
        maxSoFar = 0
        arr = letters[letter]
        
        for (j, pos) in enumerate(arr):
            if not j:
                cur = 1
            elif pos - arr[j - 1] == 1:
                cur += 1
            else:
                if not discarded and prev:
                    discarded = True
                elif not discarded and pos - arr[j - 1] > 2:
                    discarded = True
                
                if prev + cur > maxSoFar:
                    maxSoFar = prev + cur
                
                if pos - arr[j - 1] == 2:
                    prev = cur
                    cur = 1
                else:
                    prev = 0
                    cur = 1
        
        if prev + cur > maxSoFar:
            maxSoFar = prev + cur
        
        if discarded:
            maxSoFar += 1
        
        if maxSoFar > ans:
            ans = maxSoFar
    
    return ans