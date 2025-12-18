"""
QUESTION:
Given two strings of lowercase alphabets and a value K, your task is to complete the given function which tells if  two strings are K-anagrams of each other or not.
Two strings are called K-anagrams if both of the below conditions are true.
1. Both have same number of characters.
2. Two strings can become anagram by changing at most K characters in a string.
Example:
Input:
str1 = "fodr", str2="gork"
k = 2
Output:
1
Explanation: Can change fd to gk
Your Task:
Since this is a function problem, you don't need to take any input. Just complete the given function areKAnagrams that returns true if the strings can be turned into K-anagrams, else return false.
Constraints:
1 ≤ length of String ≤ 10^{5}
1 ≤ K ≤ length of String
"""

from collections import Counter

def are_k_anagrams(str1: str, str2: str, k: int) -> bool:
    # Check if both strings have the same length
    if len(str1) != len(str2):
        return False
    
    # Count the frequency of each character in both strings
    count1 = Counter(str1)
    count2 = Counter(str2)
    
    # Calculate the number of characters that need to be changed
    mismatch_count = 0
    for char in count2:
        if count2[char] > count1.get(char, 0):
            mismatch_count += count2[char] - count1.get(char, 0)
    
    # Check if the number of changes required is within the allowed limit
    return mismatch_count <= k