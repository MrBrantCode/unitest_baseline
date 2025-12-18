"""
QUESTION:
Your are given a string $S$ containing only lowercase letter and a array of character $arr$. Find whether the given string only contains characters from the given character array. 
Print $1$ if the string contains characters from the given array only else print $0$.
Note: string contains characters in lower case only.

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- Each testcase contains- 
a string $S$ of lowercase letter
a integer $n$ denoting length of character array $arr$
next line contains $n$ space separated characters.

-----Output:-----
For each testcase, Print $1$ if the string contains characters from the given array only else print $0$.

-----Constraints-----
- $1 \leq T \leq 1000$
- $0 \leq n \leq 10^5$

-----Sample Input:-----
3
abcd
4
a b c d
aabbbcccdddd
4
a b c d
acd
3
a b d

-----Sample Output:-----
1
1
0
"""

def contains_only_allowed_characters(S: str, arr: list) -> bool:
    """
    Checks if the string S contains only characters from the given array arr.

    Parameters:
    - S (str): The string to be checked.
    - arr (list): The array of characters to check against.

    Returns:
    - bool: True if S contains only characters from arr, otherwise False.
    """
    # Convert the string S to a set of characters
    S_set = set(S)
    
    # Convert the array arr to a set of characters
    arr_set = set(arr)
    
    # Check if every character in S is in arr
    for char in S_set:
        if char not in arr_set:
            return False
    
    return True