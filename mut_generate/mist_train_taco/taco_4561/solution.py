"""
QUESTION:
The problem is to check whether the decimal representation of a given binary number is divisible by 5 or not.
Example 1:
Input: bin = "1010"
Output: "Yes"
Explanation: Decimal equivalent is
10 which is divisible by 5.
Ã¢â¬â¹Example 2:
Input: bin = "1110"
Output: "No"
Explanation: Decimal equivalent is
14 which is not divisible by 5.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function isDivisibleBy5() which takes the string bin as inputs and returns the "Yes" if binary number is divisible by 5, else returns "No".
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |S| ≤ 10^{5}
"""

def is_divisible_by_5(bin_str: str) -> str:
    """
    Check if the decimal representation of a given binary number is divisible by 5.

    Parameters:
    bin_str (str): The binary number as a string.

    Returns:
    str: "Yes" if the decimal equivalent is divisible by 5, otherwise "No".
    """
    decimal_value = int(bin_str, 2)
    if decimal_value % 5 == 0:
        return 'Yes'
    return 'No'