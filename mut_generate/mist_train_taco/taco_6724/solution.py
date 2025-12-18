"""
QUESTION:
As we all know, Chef is cooking string for long days, his new discovery on string is the longest common pattern length. The longest common pattern length between two strings is the maximum number of characters that both strings have in common. Characters are case sensitive, that is, lower case and upper case characters are considered as different. Note that characters can repeat in a string and a character might have one or more occurrence in common between two strings. For example, if Chef has two strings A = "Codechef" and B = "elfedcc", then the longest common pattern length of A and B is 5 (common characters are c, d, e, e, f).
Chef wants to test you with the problem described above. He will give you two strings of Latin alphabets and digits, return him the longest common pattern length.

-----Input-----
The first line of the input contains an integer T, denoting the number of test cases. Then the description of T test cases follows.
The first line of each test case contains a string A. The next line contains another character string B.

-----Output-----
For each test case, output a single line containing a single integer, the longest common pattern length between A and B.

-----Constraints-----
- 1 ≤ T ≤ 100
- 1 ≤ |A|, |B| ≤ 10000 (104), where |S| denotes the length of the string S
- Both of A and B can contain only alphabet characters (both lower and upper case) and digits

-----Example-----
Input:
4
abcd
xyz
abcd
bcda
aabc
acaa
Codechef
elfedcc

Output:
0
4
3
5

-----Explanation-----
Example case 1. There is no common character.
Example case 2. All the characters are same.
Example case 3. Three characters (a, a and c) are same.
Example case 4. This sample is mentioned by the statement.
"""

def longest_common_pattern_length(A: str, B: str) -> int:
    # Convert strings to lists of characters
    list_A = list(A)
    list_B = list(B)
    
    # Create a set of unique characters from A
    unique_chars_A = set(list_A)
    
    # Initialize the count of common characters
    common_count = 0
    
    # Iterate over each unique character in A
    for char in unique_chars_A:
        # Count the occurrences of the character in both A and B
        count_in_A = list_A.count(char)
        count_in_B = list_B.count(char)
        
        # Add the minimum of the two counts to the common count
        common_count += min(count_in_A, count_in_B)
    
    return common_count