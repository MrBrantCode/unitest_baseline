"""
QUESTION:
Given a string s. You should re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.

In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.
Return the result string after sorting s with this algorithm.
 
Example 1:
Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

Example 2:
Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.

Example 3:
Input: s = "leetcode"
Output: "cdelotee"

Example 4:
Input: s = "ggggggg"
Output: "ggggggg"

Example 5:
Input: s = "spo"
Output: "ops"

 
Constraints:

1 <= s.length <= 500
s contains only lower-case English letters.
"""

def reorder_string(s: str) -> str:
    # Step 1: Create a sorted list of unique characters in the string
    suniq = sorted(set(s))
    
    # Step 2: Determine the maximum count of any character in the string
    max_count = max(s.count(char) for char in suniq)
    
    # Step 3: Initialize a list to keep track of the count of each character used
    chr_count = [0] * len(suniq)
    
    # Step 4: Initialize the result string
    result = ''
    
    # Step 5: Perform the re-ordering process
    for _ in range(max_count):
        # Append characters in ascending order
        for i in range(len(suniq)):
            if chr_count[i] < s.count(suniq[i]):
                result += suniq[i]
                chr_count[i] += 1
        
        # Append characters in descending order
        for i in range(len(suniq) - 1, -1, -1):
            if chr_count[i] < s.count(suniq[i]):
                result += suniq[i]
                chr_count[i] += 1
    
    return result