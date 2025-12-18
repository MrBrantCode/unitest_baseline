"""
QUESTION:
You are given a string str of length n. You want to choose a non-zero integer k (k<=n), such that you can perform the following operation:
Take the prefix of the string of length k and append the reverse of it to itself.
Your task is to find the lexicographically smallest string you can get.
Example 1:
Input:
str = "bvdfndkn"
Output:
bb
Explanation:
If we choose k=1, prefix of length k will be "b", reverse of
this prefix will be "b" itself, when we append both we get "bb",
"bb" is the lexicographically smallest string you can get.
If you choose k>1, the resulting string will not be 
lexicographically smaller than "bb".
Example 2:
Input:
str = "casd"
Output:
caac
Explanation:
If we choose k=2, prefix of length k will be "ca", reverse of
this prefix will be "ac", when we append both we get "caac",
"caac" is the lexicographically smallest string you can get.
Your Task:
You don't need to read input or print anything. Your task is to complete the function stringMirror() which takes a String str as input, and returns the lexicographically smallest string.
Expected Time Complexity: O(|str|)
Expected Space Complexity: O(|str|)
Constraints:
1 <= |str| <= 10^{5}
"""

def find_lexicographically_smallest_mirror(str: str) -> str:
    # Initialize the variable to store the prefix
    var = str[0]
    
    # Iterate through the string to find the appropriate prefix
    for i in range(1, len(str)):
        # If the first two characters are the same, break early
        if str[0] == str[1]:
            break
        # If the current character is less than or equal to the previous character, add it to the prefix
        if str[i] <= str[i - 1]:
            var += str[i]
        else:
            break
    
    # Append the reverse of the prefix to itself
    var += var[::-1]
    
    # Return the resulting lexicographically smallest string
    return var