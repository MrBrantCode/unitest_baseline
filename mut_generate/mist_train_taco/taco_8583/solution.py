"""
QUESTION:
One day, Chef prepared D brand new dishes. He named the i-th dish by a string Si. After the cooking, he decided to categorize each of these D dishes as special or not.

A dish Si is called special if it's name (i.e. the string Si) can be represented in the form of a double string by removing at most one (possibly zero) character from it's name from any position. 

A string is called a double string if it can be represented as a concatenation of two identical, non-empty strings. 
e.g. "abab" is a double string as it can be represented as "ab" + "ab" where + operation denotes concatenation. 
Similarly, "aa", "abcabc" are double strings whereas "a", "abba", "abc" are not.

-----Input-----
- First line of the input contains an integer D denoting the number of dishes prepared by Chef on that day.
- Each of the next D lines will contain description of a dish. 
	
- The i-th line contains the name of i-th dish Si.
	

-----Output-----
For each of the D dishes, print a single line containing "YES" or "NO" (without quotes) denoting whether the dish can be called as a special or not.

-----Constraints-----
- 1 ≤ D ≤ 106
- 1 ≤ |Si| ≤ 106.
- Each character of string Si will be lower case English alphabet (i.e. from 'a' to 'z').

-----Subtasks-----
Subtask #1 : (20 points)
- Sum of |Si| in an input file doesn't exceed 2 * 103

Subtask 2 : (80 points) 
- Sum of |Si| in an input file doesn't exceed 2 * 106

-----Example-----
Input:
3
aba
abac
abcd

Output:
YES
NO
NO


-----Explanation-----
Example case 1.
We can remove the character at position 1 (0-based index) to get "aa" which is a double string. Hence, it is a special dish.

Example case 2.
It is not possible to remove the character at any of the position to get the double string. Hence, it is not a special dish.
"""

def is_special_dish(s: str) -> str:
    def is_subseq(s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        i = 0
        j = 0
        while i < m and j < n:
            if s1[i] == s2[j]:
                i += 1
            j += 1
        return i == m

    def is_good(s: str) -> bool:
        n = len(s)
        return s[0:n // 2] == s[n // 2:]

    n = len(s)
    if n == 1:
        return 'NO'
    
    if n % 2 == 0:
        if s[0:n // 2] == s[n // 2:]:
            return 'YES'
        else:
            return 'NO'
    else:
        h = n // 2
        if is_subseq(s[0:h], s[h:]) or is_subseq(s[h + 1:], s[0:h + 1]) or is_good(s[0:n // 2] + s[n // 2 + 1:]):
            return 'YES'
        else:
            return 'NO'