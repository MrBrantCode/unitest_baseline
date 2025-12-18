"""
QUESTION:
Polycarp has interviewed Oleg and has written the interview down without punctuation marks and spaces to save time. Thus, the interview is now a string s consisting of n lowercase English letters.

There is a filler word ogo in Oleg's speech. All words that can be obtained from ogo by adding go several times to the end of it are also considered to be fillers. For example, the words ogo, ogogo, ogogogo are fillers, but the words go, og, ogog, ogogog and oggo are not fillers.

The fillers have maximal size, for example, for ogogoo speech we can't consider ogo a filler and goo as a normal phrase. We should consider ogogo as a filler here.

To print the interview, Polycarp has to replace each of the fillers with three asterisks. Note that a filler word is replaced with exactly three asterisks regardless of its length.

Polycarp has dealt with this problem in no time. Can you do the same? The clock is ticking!


-----Input-----

The first line contains a positive integer n (1 ≤ n ≤ 100) — the length of the interview.

The second line contains the string s of length n, consisting of lowercase English letters.


-----Output-----

Print the interview text after the replacement of each of the fillers with "***". It is allowed for the substring "***" to have several consecutive occurences.


-----Examples-----
Input
7
aogogob

Output
a***b

Input
13
ogogmgogogogo

Output
***gmg***

Input
9
ogoogoogo

Output
*********



-----Note-----

The first sample contains one filler word ogogo, so the interview for printing is "a***b".

The second sample contains two fillers ogo and ogogogo. Thus, the interview is transformed to "***gmg***".
"""

def replace_fillers(n: int, s: str) -> str:
    """
    Replaces all occurrences of the filler words in the string `s` with "***".

    Parameters:
    - n (int): The length of the string `s`.
    - s (str): The string containing the interview text.

    Returns:
    - str: The modified string with fillers replaced by "***".
    """
    # Replace the initial 'ogo' with '***'
    s = s.replace('ogo', '***')
    
    # Replace any '*go' sequences with '*'
    while '*go' in s:
        s = s.replace('*go', '*')
    
    # Replace any '***g***' sequences with '***'
    while '***g***' in s:
        s = s.replace('***g***', '***')
    
    return s