"""
QUESTION:
Vitya has just started learning Berlanese language. It is known that Berlanese uses the Latin alphabet. Vowel letters are "a", "o", "u", "i", and "e". Other letters are consonant.

In Berlanese, there has to be a vowel after every consonant, but there can be any letter after any vowel. The only exception is a consonant "n"; after this letter, there can be any letter (not only a vowel) or there can be no letter at all. For example, the words "harakiri", "yupie", "man", and "nbo" are Berlanese while the words "horse", "king", "my", and "nz" are not.

Help Vitya find out if a word $s$ is Berlanese.


-----Input-----

The first line of the input contains the string $s$ consisting of $|s|$ ($1\leq |s|\leq 100$) lowercase Latin letters.


-----Output-----

Print "YES" (without quotes) if there is a vowel after every consonant except "n", otherwise print "NO".

You can print each letter in any case (upper or lower).


-----Examples-----
Input
sumimasen

Output
YES

Input
ninja

Output
YES

Input
codeforces

Output
NO



-----Note-----

In the first and second samples, a vowel goes after each consonant except "n", so the word is Berlanese.

In the third sample, the consonant "c" goes after the consonant "r", and the consonant "s" stands on the end, so the word is not Berlanese.
"""

def is_berlanese(s: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    flag = True
    
    for i in range(len(s) - 1):
        if s[i] == 'n' or s[i] in vowels:
            continue
        if s[i + 1] not in vowels:
            flag = False
            break
    
    if s[-1] not in vowels and s[-1] != 'n':
        flag = False
    
    return "YES" if flag else "NO"