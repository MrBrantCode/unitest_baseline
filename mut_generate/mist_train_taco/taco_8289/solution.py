"""
QUESTION:
Given are strings S and T. Consider changing S to T by repeating the operation below. Find the minimum number of operations required to do so.
Operation: Choose one character of S and replace it with a different character.

-----Constraints-----
 - S and T have lengths between 1 and 2\times 10^5 (inclusive).
 - S and T consists of lowercase English letters.
 - S and T have equal lengths.

-----Input-----
Input is given from Standard Input in the following format:
S
T

-----Output-----
Print the answer.

-----Sample Input-----
cupofcoffee
cupofhottea

-----Sample Output-----
4

We can achieve the objective in four operations, such as the following:
 - First, replace the sixth character c with h.
 - Second, replace the eighth character f with t.
 - Third, replace the ninth character f with t.
 - Fourth, replace the eleventh character e with a.
"""

def min_operations_to_transform(S: str, T: str) -> int:
    """
    Calculate the minimum number of operations required to transform string S into string T.
    Each operation consists of replacing one character of S with a different character.

    Parameters:
    - S (str): The initial string.
    - T (str): The target string.

    Returns:
    - int: The minimum number of operations required.
    """
    # Initialize the count of operations
    operations_count = 0
    
    # Iterate through each character in the strings
    for i in range(len(S)):
        if S[i] != T[i]:
            operations_count += 1
    
    return operations_count