"""
QUESTION:
Given a  number N such that it may contain many continuous digits. Find the number of ways to spell the number.
For example, consider 8884441100, one can spell it simply as triple eight triple four double two and double zero. One can also spell as double eight, eight, four, double four, two, two, double zero.
 
Example 1:
Input:
N = 100
Output:
2
Explanation:
The number 100 has only 2 possibilities, 
1) one zero zero 
2) one double zero.
Example 2:
Input:
N = 11112
Output:
8
Explanation:
1 1 1 1 2, 11 1 1 2, 1 1 11 2, 1 11 1 2,
11 11 2, 1 111 2, 111 1 2, 1111 2
Example 3:
Input:
N = 12345
Output:
1
Explanation:
The number 12345 has only 1 possibility, 
one two three four five
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function differentWaysToSpell() which takes a String N as input and returns the number of possible ways.
 
Expected Time Complexity: O(|N|)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= |N| <= 10^{50}
"""

def calculate_different_ways_to_spell(N: str) -> int:
    """
    Calculate the number of different ways to spell a given number.

    Args:
    N (str): The input number as a string.

    Returns:
    int: The number of different ways to spell the input number.
    """
    result = 1
    count = 1
    for i in range(1, len(N)):
        if N[i - 1] == N[i]:
            count += 1
        else:
            result *= 2 ** (count - 1)
            count = 1
    return result * 2 ** (count - 1)