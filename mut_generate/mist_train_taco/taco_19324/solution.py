"""
QUESTION:
Our hacker, Little Stuart lately has been fascinated by ancient puzzles. One day going through some really old books he finds something scribbled on the corner of a page. Now Little Stuart believes that the scribbled text is more mysterious than it originally looks, so he decides to find every occurrence of all the permutations of the scribbled text in the entire book. Since this is a huge task, Little Stuart needs your help, he needs you to only figure out if any permutation of the scribbled text exists in the given text string, so he can save time and analyze only those text strings where a valid permutation is present.

Input:
First line contains number of test cases T.Each test case contains two lines ,first line contains  pattern and next line contains a text string. All characters in both the strings are in lowercase only [a-z].

Output:
For each test case print "YES" or "NO" (quotes for clarity) depending on whether any permutation of the pattern exists in the text string.

Constraints:
1 ≤ T ≤ 100
1 ≤ |Pattern| ≤ 1000
1 ≤ |Text String| ≤ 100000  

SAMPLE INPUT
3
hack
indiahacks
code
eddy
coder
iamredoc

SAMPLE OUTPUT
YES
NO
YES
"""

def contains_permutation(pattern: str, text: str) -> str:
    """
    Checks if any permutation of the pattern exists in the text.

    Parameters:
    pattern (str): The pattern string for which we need to check if any permutation exists in the text.
    text (str): The text string in which we need to search for any permutation of the pattern.

    Returns:
    str: "YES" if any permutation of the pattern exists in the text, otherwise "NO".
    """
    from collections import Counter
    
    pattern_len = len(pattern)
    text_len = len(text)
    
    if pattern_len > text_len:
        return "NO"
    
    pattern_counter = Counter(pattern)
    window_counter = Counter(text[:pattern_len])
    
    if pattern_counter == window_counter:
        return "YES"
    
    for i in range(pattern_len, text_len):
        start_char = text[i - pattern_len]
        new_char = text[i]
        
        window_counter[start_char] -= 1
        if window_counter[start_char] == 0:
            del window_counter[start_char]
        
        window_counter[new_char] += 1
        
        if pattern_counter == window_counter:
            return "YES"
    
    return "NO"