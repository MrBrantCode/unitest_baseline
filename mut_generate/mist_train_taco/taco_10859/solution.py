"""
QUESTION:
You are given a number str(in string format) in hexadecimal. A new number can be made from the number str by selecting any subsequence of it (in HexaDecimal) and rearranging it.
You have tell the number of distinct numbers that can be made from number n.
 
Example 1:
Input: str = "1F"
Output: 4
Explanation: For 1F possible combination are 
1, F, 1F, F1.
Example 2:
Input: str = "1FF"
Output: 8
Explanation: For 1FF possible combinations are
1, F, 1F, F1, FF, 1FF, F1F, FF1.
 
Your Task:
You don't need to read or print anyhthing. Your task is to complete the function countOfDistinctNo() which takes str in string format as input and returns the total possible combination modulo 10^{9}+7.
 
Expected Time Compelxity: O(L*L) where L is the length of the string str.
Expected Space Complexity: O(L)
 
Constraints:
1 <= n <= 2^{8000} where n = str in decimal.
"""

import itertools

def count_of_distinct_numbers(hex_string):
    """
    This function calculates the number of distinct numbers that can be made from a given hexadecimal string.
    
    Parameters:
    hex_string (str): A string representing a hexadecimal number.
    
    Returns:
    int: The number of distinct numbers that can be made from the given hexadecimal string modulo 10^9 + 7.
    """
    # Remove duplicate characters while preserving the original order
    distinct_chars = []
    for char in hex_string:
        if char not in distinct_chars:
            distinct_chars.append(char)
    
    # Calculate the number of distinct numbers using the concept of combinations
    total_combinations = 0
    for i in range(1, len(distinct_chars) + 1):
        total_combinations += len(list(itertools.permutations(distinct_chars, i)))
    
    # Add 1 to account for the empty string
    total_combinations += 1
    
    # Return the result modulo 10^9 + 7
    return total_combinations % (10**9 + 7)