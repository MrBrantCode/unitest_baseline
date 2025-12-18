"""
QUESTION:
Given a string S consisting of only uppercase and lowercase characters. The task is to sort uppercase and lowercase letters separately such that if the i_{th} place in the original string had an Uppercase character then it should not have a lowercase character after being sorted and vice versa.
Example 1:
Input:
N = 12
S = defRTSersUXI
Output: deeIRSfrsTUX
Explanation: Sorted form of given string
with the same case of character as that
in original string is deeIRSfrsTUX
Example 2:
Input:
N = 6
S = srbDKi
Output: birDKs
Explanation: Sorted form of given string
with the same case of character will
result in output as birDKs.
Your Task:
You only need to complete the function caseSort that takes a string str and length of the string n and returns sorted string.
Expected Time Complexity: O(Nlog(N)).
Expected Auxiliary Space: O(N).
Constraints: 
1 ≤ N ≤ 10^{5}
"""

def case_sort(s: str, n: int) -> str:
    # Separate lowercase and uppercase characters
    lower_chars = []
    upper_chars = []
    
    for char in s:
        if char.isupper():
            upper_chars.append(char)
        else:
            lower_chars.append(char)
    
    # Sort the lowercase and uppercase characters
    lower_chars.sort()
    upper_chars.sort()
    
    # Reconstruct the sorted string
    sorted_string = []
    lower_index = 0
    upper_index = 0
    
    for char in s:
        if char.isupper():
            sorted_string.append(upper_chars[upper_index])
            upper_index += 1
        else:
            sorted_string.append(lower_chars[lower_index])
            lower_index += 1
    
    return ''.join(sorted_string)