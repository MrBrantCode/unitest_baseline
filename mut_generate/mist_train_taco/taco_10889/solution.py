"""
QUESTION:
Given a number N, if the number is between 1 and 10 both inclusive then return the number in words (Lower case English Alphabets) otherwise return "not in range".
 
Example 1:
Input:
5
Output:
five
 
Example 2:
Input:
11
Output:
not in range
 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function isInRange() which takes an integer and if the number is between 1 and 10 both inclusive then return the number in words otherwise return "not in range".
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1<=N<=10000
"""

def number_to_words(N: int) -> str:
    switcher = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten'
    }
    return switcher.get(N, 'not in range')