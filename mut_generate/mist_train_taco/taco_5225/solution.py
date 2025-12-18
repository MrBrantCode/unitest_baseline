"""
QUESTION:
A: A-Z Cat / A-Z Cat

story

Aizunyan is a second-year student who belongs to the programming contest club of Wakagamatsu High School, commonly known as the Prokon club. It's so cute. Aizu Nyan was asked by her friend Joy to take care of her cat. It is a rare cat called A-Z cat. Aizunyan named the A-Z cat he had entrusted to him as "Aizunyan No. 2" (without permission), and he was very much loved.

A-Z cats are said to prefer strings that meet certain conditions. Then, when Aizunyan gave a character string as a trial, Aizunyan No. 2 had a satisfying expression after cutting a part of the character string with his nails. Apparently, I'm trying to rewrite it to my favorite character string.

D, who is crazy about Aizu Nyan, who is cute like an angel, found out the character string conditions that A-Z Cat likes for Aizu Nyan. It is a string in which'A'and'Z'are repeated alternately, and a string that starts with'A' and ends with'Z'. The A-Z cat is so smart that it tries to convert it to a string of your choice with minimal erasing. D, who wants to look good, decided to write a program to find out what kind of string the A-Z cat would convert from a given string consisting only of'A'and'Z'.

problem

Given a string S consisting only of uppercase letters. By deleting any number of S characters as much as you like, you can create a string in which'A'and'Z' appear alternately, and start with'A' and end with'Z'. Find the character string obtained when the number of deletions is minimized.

Input format

The string S is given on one line as input. S consists of uppercase letters only and satisfies 1 ≤ | S | ≤ 20.

Output format

Output the string that is obtained by deleting the minimum number of characters for S, in which'A'and'Z' appear alternately, and start with'A' and end with'Z' on one line. If no character string that meets the conditions is obtained by deleting any character, output -1 on one line.

Input example 1


AIZUNYAN PEROPERO

Output example 1


AZ

Input example 2


AZAZ

Output example 2


AZAZ

Input example 3


ZDDYAZAWABDDZAZPIDDA

Output example 3


AZAZAZ

Input example 4


ZZZZAAAAAA

Output example 4


-1





Example

Input

AIZUNYANPEROPERO


Output

AZ
"""

def find_minimal_alternating_az_string(s: str) -> str:
    a, c = 1, 0
    for x in s:
        if x == 'A':
            a = 0
        elif x == 'Z' and (not a):
            a, c = 1, c + 1
    return 'AZ' * c if c else -1