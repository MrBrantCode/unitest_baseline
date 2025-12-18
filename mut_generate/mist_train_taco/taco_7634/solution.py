"""
QUESTION:
We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice is taking a cryptography class and finding anagrams to be very useful. She decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number? 

Given two strings, $\mbox{s1}$ and $\mbox{s2}$, that may not be of the same length, determine the minimum number of character deletions required to make $\mbox{s1}$ and $\mbox{s2}$ anagrams. Any characters can be deleted from either of the strings. 

Example. 

$\textit{s1}=\texttt{abc}$ 

$s2=\textbf{amnop}$     

The only characters that match are the $\mbox{a}$'s so we have to remove $\mathbf{bc}$ from $\mbox{s1}$ and $\textbf{mnop}$ from $\mbox{s2}$ for a total of $\boldsymbol{6}$ deletions.  

Function Description  

Complete the makingAnagrams function in the editor below.    

makingAnagrams has the following parameter(s):  

string s1: a string  
string s2: a string   

Returns   

int: the minimum number of deletions needed   

Input Format

The first line contains a single string, $\mbox{s1}$. 

The second line contains a single string, $\mbox{s2}$.

Constraints

$1\leq|s1|,|s2|\leq10^4$  
It is guaranteed that $\mbox{s1}$ and $\mbox{s2}$ consist of lowercase English letters, ascii[a-z].

Sample Input
cde
abc

Sample Output
4

Explanation

Delete the following characters from our two strings to turn them into anagrams:

Remove d and e from cde to get c.
Remove a and b from abc to get c.

$4$ characters have to be deleted to make both strings anagrams.
"""

def minimum_deletions_to_anagram(s1: str, s2: str) -> int:
    from collections import Counter
    
    # Count the frequency of each character in both strings
    count_s1 = Counter(s1)
    count_s2 = Counter(s2)
    
    # Calculate the total deletions required
    deletions = 0
    for char in set(count_s1.keys()).union(count_s2.keys()):
        deletions += abs(count_s1[char] - count_s2[char])
    
    return deletions