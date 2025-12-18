"""
QUESTION:
There is a sequence of words in CamelCase as a string of letters, $\boldsymbol{\mathrm{~S~}}$, having the following properties:

It is a concatenation of one or more words consisting of English letters.
All letters in the first word are lowercase. 
For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.

Given $\boldsymbol{\mathrm{~S~}}$, determine the number of words in $\boldsymbol{\mathrm{~S~}}$.

Example 

$s=one Two Thee$  

There are $3$ words in the string: 'one', 'Two', 'Three'.  

Function Description

Complete the camelcase function in the editor below.  

camelcase has the following parameter(s):

string s: the string to analyze   

Returns  

int: the number of words in $\boldsymbol{\mathrm{~S~}}$  

Input Format

A single line containing string $\boldsymbol{\mathrm{~S~}}$.

Constraints

$1\leq\text{length of s}\leq10^5$

Sample Input
saveChangesInTheEditor

Sample Output
5

Explanation

String $\boldsymbol{\mathrm{~S~}}$ contains five words:

save
Changes
In
The
Editor

Need help? Try this problem first to get familiar with HackerRank environment.
"""

def count_camel_case_words(s: str) -> int:
    """
    Counts the number of words in a CamelCase string.

    Parameters:
    s (str): The CamelCase string to analyze.

    Returns:
    int: The number of words in the CamelCase string.
    """
    if not s:
        return 0
    
    word_count = 1
    for char in s:
        if char.isupper():
            word_count += 1
    
    return word_count