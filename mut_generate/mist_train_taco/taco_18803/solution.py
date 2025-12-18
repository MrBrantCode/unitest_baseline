"""
QUESTION:
Professor McGonagall teaches transfiguration at Hogwarts. She has given Harry the task of changing himself into a cat. She explains that the trick is to analyze your own DNA and change it into the DNA of a cat. The transfigure spell can be used to pick any one character from the DNA string, remove it and insert it in the beginning. 
Help Harry calculates minimum number of times he needs to use the spell to change himself into a cat.
Example 1:
Input: 
A = "GEEKSFORGEEKS" 
B = "FORGEEKSGEEKS"
Output: 3
Explanation:The conversion can take place 
in 3 operations:
1. Pick 'R' and place it at the front, 
   A="RGEEKSFOGEEKS"
2. Pick 'O' and place it at the front, 
   A="ORGEEKSFGEEKS"
3. Pick 'F' and place it at the front, 
   A="FORGEEKSGEEKS"
Example 2:
Input: 
A = "ABC" 
B = "BCA"
Output: 2
Explanation: The conversion can take place 
in 2 operations:
1. Pick 'C' and place it at the front, 
   A = "CAB"
2. Pick 'B' and place it at the front, 
   A = "BCA"
Your Task:  
You don't need to read input or print anything. Complete the function transfigure() which takes strings A and B as input parameters and returns the minimum number of spells needed. If it is not possible to convert A to B then return -1.
Expected Time Complexity: O(max(|A|, |B|))
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |A|, |B| ≤ 10^{5}
A and B consists of lowercase and uppercase letters of english alphabet only.
"""

def min_spells_to_transfigure(A: str, B: str) -> int:
    # Check if both strings have the same length
    if len(A) != len(B):
        return -1
    
    # Create a frequency map for characters in A
    char_count = {}
    for char in A:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Decrease the count for each character in B
    for char in B:
        if char in char_count:
            char_count[char] -= 1
        else:
            # If a character in B is not in A, return -1
            return -1
    
    # Check if all counts are zero
    for count in char_count.values():
        if count != 0:
            return -1
    
    # Calculate the minimum number of spells needed
    i, j = len(A) - 1, len(B) - 1
    res = 0
    while i >= 0 and j >= 0:
        if A[i] == B[j]:
            j -= 1
        else:
            res += 1
        i -= 1
    
    return res