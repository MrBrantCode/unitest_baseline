"""
QUESTION:
Given a string s which contains only lower alphabetic characters, check if it is possible to remove at most one character from this string in such a way that frequency of each distinct character becomes same in the string.
Example 1:
Input:
s = xyyz
Output: 1 
Explanation: Removing one 'y' will make 
frequency of each letter 1.
Example 2:
Input:
s = xxxxyyzz
Output: 0
Explanation: Frequency can not be made same 
same by removing just 1 character.
Your Task:  
You dont need to read input or print anything. Complete the function sameFreq() which takes a string as input parameter and returns a boolean value denoting if same frequency is possible or not.
Note: The driver code print 1 if the value returned is true, otherwise 0.
Expected Time Complexity: O(N) where N is length of str
Expected Auxiliary Space: O(1)
Constraints:
1 <= str.length() <= 10^{4}
"""

def can_make_same_frequency(s: str) -> bool:
    from collections import Counter
    
    # Count the frequency of each character
    freq_count = Counter(s)
    
    # Get the frequency values
    freq_values = list(freq_count.values())
    
    # If all frequencies are already the same, return True
    if len(set(freq_values)) == 1:
        return True
    
    # Check if removing one character can make all frequencies the same
    for char in freq_count:
        freq_count[char] -= 1
        if freq_count[char] == 0:
            del freq_count[char]
        
        # Get the new frequency values after removing one character
        new_freq_values = list(freq_count.values())
        
        # Check if all new frequencies are the same
        if len(set(new_freq_values)) == 1:
            return True
        
        # Restore the original frequency count
        freq_count[char] += 1
    
    return False