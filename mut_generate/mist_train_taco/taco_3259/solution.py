"""
QUESTION:
You are given two strings $s$ and $t$. In a single move, you can choose any of two strings and delete the first (that is, the leftmost) character. After a move, the length of the string decreases by $1$. You can't choose a string if it is empty.

For example:  by applying a move to the string "where", the result is the string "here",  by applying a move to the string "a", the result is an empty string "". 

You are required to make two given strings equal using the fewest number of moves. It is possible that, in the end, both strings will be equal to the empty string, and so, are equal to each other. In this case, the answer is obviously the sum of the lengths of the initial strings.

Write a program that finds the minimum number of moves to make two given strings $s$ and $t$ equal.


-----Input-----

The first line of the input contains $s$. In the second line of the input contains $t$. Both strings consist only of lowercase Latin letters. The number of letters in each string is between 1 and $2\cdot10^5$, inclusive.


-----Output-----

Output the fewest number of moves required. It is possible that, in the end, both strings will be equal to the empty string, and so, are equal to each other. In this case, the answer is obviously the sum of the lengths of the given strings.


-----Examples-----
Input
test
west

Output
2

Input
codeforces
yes

Output
9

Input
test
yes

Output
7

Input
b
ab

Output
1



-----Note-----

In the first example, you should apply the move once to the first string and apply the move once to the second string. As a result, both strings will be equal to "est".

In the second example, the move should be applied to the string "codeforces" $8$ times. As a result, the string becomes "codeforces" $\to$ "es". The move should be applied to the string "yes" once. The result is the same string "yes" $\to$ "es".

In the third example, you can make the strings equal only by completely deleting them. That is, in the end, both strings will be empty.

In the fourth example, the first character of the second string should be deleted.
"""

def min_moves_to_equal_strings(s: str, t: str) -> int:
    # Determine the lengths of the strings
    len_s = len(s)
    len_t = len(t)
    
    # Find the minimum length between the two strings
    min_len = min(len_s, len_t)
    
    # Initialize the index for comparison
    i = 0
    
    # Compare characters from the end of both strings
    while i < min_len:
        if s[-1 - i] != t[-1 - i]:
            break
        i += 1
    
    # Calculate the minimum number of moves
    moves = 2 * (min_len - i) + abs(len_s - len_t)
    
    return moves