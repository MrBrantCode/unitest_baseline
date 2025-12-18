"""
QUESTION:
Given a list of names, display the longest name.
Example:
Input:
N = 5
names[] = { "Geek", "Geeks", "Geeksfor",
  "GeeksforGeek", "GeeksforGeeks" }
Output:
GeeksforGeeks
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function longest() which takes the array names[] and its size N as inputs and returns the Longest name in the list of names.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 100
1 <= |length of name| <= 1000
"""

def find_longest_name(names, n):
    # Initialize a variable to keep track of the longest name
    longest_name = ""
    
    # Iterate through each name in the list
    for name in names:
        # Update the longest_name if the current name is longer
        if len(name) > len(longest_name):
            longest_name = name
    
    # Return the longest name found
    return longest_name