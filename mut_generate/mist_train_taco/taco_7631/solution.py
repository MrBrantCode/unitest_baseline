"""
QUESTION:
Dothraki are planning an attack to usurp King Robert's throne. King Robert learns of this conspiracy from Raven and plans to lock the single door through which the enemy can enter his kingdom.

But, to lock the door he needs a key that is an anagram of a palindrome.  He starts to go through his box of strings, checking to see if they can be rearranged into a palindrome.  Given a string, determine if it can be rearranged into a palindrome.  Return the string YES or NO.  

Example 

$s=\text{'aabbccdd'}$  

One way this can be arranged into a palindrome is $abcddcba$.  Return YES.

Function Description 

Complete the gameOfThrones function below. 

gameOfThrones has the following parameter(s):  

string s: a string to analyze   

Returns  

string:  either YES or NO   

Input Format

A single line which contains $\boldsymbol{\mathrm{~S~}}$.

Constraints

$1\leq$ |s| $\leq10^5$  
$\boldsymbol{\mathrm{~S~}}$ contains only lowercase letters in the range $a s c i i[a\ldots z]$

Sample Input 0
aaabbbb

Sample Output 0
YES

Explanation 0

A palindromic permutation of the given string is bbaaabb.   

Sample Input 1
cdefghmnopqrstuvw

Sample Output 1
NO

Explanation 1

Palindromes longer than 1 character are made up of pairs of characters.  There are none here.  

Sample Input 2
cdcdcdcdeeeef

Sample Output 2
YES

Explanation 2

An example palindrome from the string:  ddcceefeeccdd.
"""

def can_form_palindrome(s: str) -> str:
    character_count = {}
    
    # Count the frequency of each character in the string
    for char in s:
        if char not in character_count:
            character_count[char] = s.count(char)
    
    odd_counts = 0
    
    # Count how many characters have an odd frequency
    for count in character_count.values():
        if count % 2 == 1:
            odd_counts += 1
    
    # A string can be rearranged into a palindrome if at most one character has an odd frequency
    if odd_counts > 1:
        return 'NO'
    else:
        return 'YES'