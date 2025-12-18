"""
QUESTION:
Little Jhool considers Jaadu to be a very close friend of his. But, he ends up having some misunderstanding with him a lot of times, because Jaadu's English isn't perfect, and Little Jhool sucks at the language Jaadu speaks. So, he's in a fix - since he knows that Jaadu has got magical powers, he asks him to help so as to clear all the issues they end up having with their friendship.

Now, Jaadu can only focus at one task, so to fix these language issues he comes up with a magical way out, but someone needs to do the rest of it; this is where Little Jhool has asked for your help.

Little Jhool says a word, and then Jaadu says another word. If any sub-string of the word said by Jaadu is a sub-string of the word said by Little Jhool, the output should be "YES", else "NO". (Without the quotes.)

Input:
First line contains number of test case T. Each test case contains two strings *Text ( Said by Jhool ) * and Pattern (Said by Jaadu ).Both strings contains only lowercase alphabets ['a'-'z'].    

Output:
For each test case print YES if any sub-string of Pattern is sub-string of Text else print NO.  

Constraints: 
1 ≤ T ≤ 5
1 ≤ |Text| ≤ 100000
1 ≤ |Pattern| ≤ 100000 

SAMPLE INPUT
2
hackerearth
hacker
hackerearth
wow
SAMPLE OUTPUT
YES
NO
"""

def check_substring_presence(text: str, pattern: str) -> str:
    # Ensure text is the longer string
    if len(text) < len(pattern):
        text, pattern = pattern, text
    
    # Check if pattern is a substring of text
    if pattern in text:
        return "YES"
    
    # If pattern length is small, check all possible substrings
    if len(pattern) < 100:
        for j in range(len(pattern)):
            for k in range(j + 1, len(pattern) + 1):
                if pattern[j:k] in text:
                    return "YES"
    
    return "NO"