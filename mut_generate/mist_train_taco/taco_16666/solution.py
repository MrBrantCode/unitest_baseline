"""
QUESTION:
You are given a string str of lower case english alphabets. You can choose any two characters in the string and replace all the occurences of the first character with the second character and replace all the occurences of the second character with the first character. Your aim is to find the lexicographically smallest string that can be obtained by doing this operation at most once.
 
Exampel 1:
Input: str = "ccad"
Output: "aacd"
Explanation: In ccad, we choose ‘a’ and ‘c’
and after doing the replacement operation 
once we get, aacd and this is the 
lexicographically smallest string possible.
Example 2:
Input: "abba"
Output: "abba"
Explanation: In abba, we can get baab after 
doing the replacement operation once for ‘a’ 
and ‘b’ but that is not lexicographically 
smaller than abba and so the answer is abba.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function LexicographicallyMinimum() which takes string str as input parameter and retruns the lexicographically minimum possible string after doing the operation.
 
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)
 
Constraints:
1 <= |str| <= 10^{4}
"""

def get_lexicographically_minimum_string(str):
    new = list(str)
    unique_chars = list(set(str))
    unique_chars.sort(reverse=True)
    
    for x in new:
        if x in unique_chars:
            if x == unique_chars[-1]:
                unique_chars.pop()
            else:
                item, repwith = x, unique_chars[-1]
                break
    else:
        return str
    
    for y, x in enumerate(new):
        if x == item:
            new[y] = repwith
        elif x == repwith:
            new[y] = item
    
    return ''.join(new)