"""
QUESTION:
Given a string of length N, made up of only uppercase characters 'R' and 'G', where 'R' stands for Red and 'G' stands for Green.Find out the minimum number of characters you need to change to make the whole string of the same colour.
Example 1:
Input:
N=5
S="RGRGR"
Output:
2
Explanation:
We need to change only the 2nd and 
4th(1-index based) characters to 'R', 
so that the whole string becomes 
the same colour.
Example 2:
Input:
N=7
S="GGGGGGR"
Output:
1
Explanation:
We need to change only the last 
character to 'G' to make the string 
same-coloured.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function RedOrGreen() which takes the Integer N and the string S as input parameters and returns the minimum number of characters that have to be swapped to make the string same-coloured.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1<=N<=10^{5}
S consists only of characters 'R' and 'G'.
"""

def min_changes_to_uniform_color(N, S):
    # Initialize a dictionary to count occurrences of 'R' and 'G'
    char_count = {'R': 0, 'G': 0}
    
    # Count the occurrences of each character in the string
    for char in S:
        char_count[char] += 1
    
    # The minimum number of changes required is the minimum of the counts of 'R' and 'G'
    return min(char_count['R'], char_count['G'])