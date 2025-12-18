"""
QUESTION:
Chef had an interesting dream last night. He dreamed of a new revolutionary chicken recipe. When he woke up today he tried very hard to reconstruct the ingredient list. But, he could only remember certain ingredients. To simplify the problem, the ingredient list can be represented by a string of lowercase characters 'a' - 'z'.
Chef can recall some characters of the ingredient list, all the others, he has forgotten. However, he is quite sure that the ingredient list was a palindrome.
You are given the ingredient list Chef dreamed last night. The forgotten characters are represented by a question mark ('?'). Count the number of ways Chef can replace the forgotten characters with characters 'a' - 'z' in such a way that resulting ingredient list is a palindrome.

-----Input-----
The first line of input contains a single integer T, the number of test cases. T lines follow, each containing a single non-empty string - the ingredient list as recalled by Chef. Whatever letters he couldn't recall are represented by a '?'.

-----Output-----
For each test case, output a single line containing the number of valid ways the ingredient list could be completed. Since the answers can be very large, output each answer modulo 10,000,009.

-----Example-----
Input:
5
?
??
ab?
a?c
aba

Output:
26
26
1
0
1

-----Constraints-----

1 ≤ T ≤ 20

1 ≤ sum of length of all input strings ≤ 1,000,000

Each input string contains only lowercase roman letters ('a' - 'z') or question marks.
"""

def count_palindrome_ways(ingredient_list: str) -> int:
    n = len(ingredient_list)
    (a, b, c) = (0, n - 1, 1)
    
    while a <= b:
        if ingredient_list[a] == '?' == ingredient_list[b]:
            c = c * 26 % 10000009
        elif ingredient_list[a] != '?' and ingredient_list[b] != '?' and (ingredient_list[a] != ingredient_list[b]):
            c = 0
            break
        a += 1
        b -= 1
    
    return c