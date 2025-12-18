"""
QUESTION:
Given a string. Count the number of Camel Case characters in it.
Example 1:
Input:
S = "ckjkUUYII"
Output: 5
Explanation: Camel Case characters present:
U, U, Y, I and I.
Ã¢â¬â¹Example 2:
Input: 
S = "abcd"
Output: 0
Explanation: No Camel Case character
present.
Your Task:
You don't need to read input or print anything. Your task is to complete the function countCamelCase() which takes the string S as input and returns the count of the camel case characters in the string.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).
Constraints:
1<=|S|<=10^{5}
"""

def count_camel_case(s: str) -> int:
    """
    Counts the number of Camel Case characters (uppercase letters) in the given string.

    Parameters:
    s (str): The input string to be checked.

    Returns:
    int: The count of camel case characters in the string.
    """
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    return count