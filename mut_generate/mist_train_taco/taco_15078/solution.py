"""
QUESTION:
Given a string, find the length of string.

Input Format:
First line contains single integer t, the number of test-cases. Each of next t lines contains a string of lower case alphabets.

Output Format:
Output t lines, each containing the single integer, length of corresponding string.

Constraints:
1 ≤ t ≤ 100
1 ≤ length of string ≤ 100

SAMPLE INPUT
2
hello
heckerearth

SAMPLE OUTPUT
5
11
"""

def calculate_string_lengths(test_cases):
    """
    Calculate the length of each string in the given list of test cases.

    Parameters:
    test_cases (list of str): A list of strings where each string is a test case.

    Returns:
    list of int: A list of integers where each integer is the length of the corresponding string in the input list.
    """
    return [len(string) for string in test_cases]