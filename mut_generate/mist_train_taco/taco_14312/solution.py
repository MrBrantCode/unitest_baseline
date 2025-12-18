"""
QUESTION:
Given a binary number in the form of string, the task is to check whether the decimal representation of the given binary number is divisible by 10 or not. The number could be very large and may not fit even in long long int.
Example 1:
Input:
bin = "1010"
Output:
1
Explanation:
The decimal representation of given 
string is 10 which is divisible by 10.
So, answer is 1.
Example 2:
Input:
bin = "10"
Output:
0
Explanation:
The decimal representation of bin is 
2, which is not divisible by 10, so 
answer is 0.
Your Task:
You don't need to read input or print anything.Your Task is to complete the function isDivisibleBy10() which takes a binary string bin as input parameter and returns 0 if the decimal representaion of bin is not divisible by 10.Otherwise it returns 1.
Expected Time Complexity:O(N)
Expected Auxillary Space:O(1)
Constraints:
1 <= |bin| <= 10^{5}
"""

def is_divisible_by_10(bin_str: str) -> int:
    """
    Checks if the decimal representation of the given binary number is divisible by 10.

    Parameters:
    bin_str (str): The binary number in string format.

    Returns:
    int: 1 if the decimal representation is divisible by 10, otherwise 0.
    """
    n = int(bin_str, 2)
    if n % 10 == 0:
        return 1
    return 0