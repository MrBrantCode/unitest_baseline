"""
QUESTION:
Given two strings s1 and s2 consisting of only lowercase characters whose anagrams are almost equal. The task is to count the number of characters which needs to be edited(delete) to make s1 equal to s2.
Example:
Input:
s1 = madame
s2 = madam
Output:
1
Explanation:
String s1 = madame, string s2 = madam. 
character 'e' in first string needs to 
be deleted to make s1 equal to s2.
 
Your Task:
Print the count of characters needed to delete to make s1 and s2 equal. Complete the given function.
Expected Time Complexity: O(max(|s1|,|s2|))
Expected Auxilary Space: O(|s1| + |s2|) 
Constraints:
1 <= s1, s2 <= 10^{4}
"""

def count_characters_to_delete(s1: str, s2: str) -> int:
    from collections import Counter
    
    # Count the frequency of each character in both strings
    count_s1 = Counter(s1)
    count_s2 = Counter(s2)
    
    # Calculate the number of deletions required
    deletions = 0
    
    # Characters in s1 that are not in s2 or have more occurrences
    for char in count_s1:
        if char not in count_s2:
            deletions += count_s1[char]
        else:
            deletions += abs(count_s1[char] - count_s2[char])
    
    # Characters in s2 that are not in s1
    for char in count_s2:
        if char not in count_s1:
            deletions += count_s2[char]
    
    return deletions