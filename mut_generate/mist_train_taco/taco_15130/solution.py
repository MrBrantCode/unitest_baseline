"""
QUESTION:
Sherlock and Watson are playing swapping game. Watson gives to Sherlock a string S on which he has performed K swaps. You need to help Sherlock in finding the original string.  
One swap on a string is performed in this way:   
Assuming 1 indexing, the i'th letter from the end is inserted
   between i'th and (i+1)'th letter from the starting.

For example, we have "contest". After one swap, it would change to "ctosnet".
Check this image:

Input: 
First line contains K, the number of swaps performed by Watson. Next line contains S, the string Watson gives to Sherlock.

Output: 
You have to print in one line the original string with which Watson had started.     

Constraints: 
1 ≤ K ≤ 10^9 
3 ≤ Length(S) ≤ 1000  
All characters in S will be small English alphabets.

SAMPLE INPUT
3
hrrkhceaate

SAMPLE OUTPUT
hackerearth

Explanation

When swapping is done on "hackerearth" 3 times, it transforms to "hrrkhceaate".
"""

def find_original_string(K, S):
    """
    Finds the original string before K swaps were performed on it.

    Parameters:
    K (int): The number of swaps performed by Watson.
    S (str): The string Watson gives to Sherlock after performing K swaps.

    Returns:
    str: The original string before any swaps were performed.
    """
    def inverted_swap(s):
        len_s = len(s)
        if len_s % 2 == 0:
            return s[::2] + s[-1::-2]
        else:
            return s[::2] + s[-2::-2]
    
    orig_s = S
    cycle_duration = 0
    
    while K > 0:
        S = inverted_swap(S)
        K -= 1
        cycle_duration += 1
        if S == orig_s:
            K = K % cycle_duration
    
    return S