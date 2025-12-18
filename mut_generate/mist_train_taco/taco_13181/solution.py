"""
QUESTION:
$Alien$ likes to give challenges to $Codezen$ team to check their implementation ability, this time he has given a string $S$ and asked to find out whether the given string is a $GOOD$ string or not.
According to the challenge $GOOD$ String is a string that has at least $3$ consecutive vowels and at least $5$ different consonants.
For example $ACQUAINTANCES$  is a $ GOOD $String ,as it contains $3$ consecutive vowels  $UAI$ and $5$ different consonants $ {C, Q, N, T, S} $
but  $ACQUAINT $ is  not ,as it contain $3$ vowels but have only $ 4$ different consonants 
${C, Q, N, T}$.

-----Input:-----
A string input is given from Standard Input that consists of only capital letters. 

-----Output:-----
Output  a single line  that  is either $GOOD$  (if string is a good string ) or $-1$(if string is not good).

-----Constraints-----
- $8 \leq S \leq 1000$

-----Sample Input 1:-----
AMBITIOUSNESS

-----Sample Output 2:-----
GOOD

-----Sample Input 2:-----
COOEY

-----Sample Output 2:-----
-1
"""

def is_good_string(s: str) -> str:
    vowels = {'A', 'E', 'I', 'O', 'U'}
    
    # Check for at least 3 consecutive vowels
    consecutive_vowels = False
    for i in range(len(s) - 2):
        if s[i] in vowels and s[i + 1] in vowels and s[i + 2] in vowels:
            consecutive_vowels = True
            break
    
    if not consecutive_vowels:
        return "-1"
    
    # Remove vowels and count distinct consonants
    consonants = set(s) - vowels
    if len(consonants) >= 5:
        return "GOOD"
    else:
        return "-1"