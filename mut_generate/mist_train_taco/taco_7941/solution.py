"""
QUESTION:
The process of mammoth's genome decoding in Berland comes to its end!

One of the few remaining tasks is to restore unrecognized nucleotides in a found chain s. Each nucleotide is coded with a capital letter of English alphabet: 'A', 'C', 'G' or 'T'. Unrecognized nucleotides are coded by a question mark '?'. Thus, s is a string consisting of letters 'A', 'C', 'G', 'T' and characters '?'.

It is known that the number of nucleotides of each of the four types in the decoded genome of mammoth in Berland should be equal.

Your task is to decode the genome and replace each unrecognized nucleotide with one of the four types so that the number of nucleotides of each of the four types becomes equal.


-----Input-----

The first line contains the integer n (4 ≤ n ≤ 255) — the length of the genome.

The second line contains the string s of length n — the coded genome. It consists of characters 'A', 'C', 'G', 'T' and '?'.


-----Output-----

If it is possible to decode the genome, print it. If there are multiple answer, print any of them. If it is not possible, print three equals signs in a row: "===" (without quotes).


-----Examples-----
Input
8
AG?C??CT

Output
AGACGTCT

Input
4
AGCT

Output
AGCT

Input
6
????G?

Output
===

Input
4
AA??

Output
===



-----Note-----

In the first example you can replace the first question mark with the letter 'A', the second question mark with the letter 'G', the third question mark with the letter 'T', then each nucleotide in the genome would be presented twice.

In the second example the genome is already decoded correctly and each nucleotide is exactly once in it.

In the third and the fourth examples it is impossible to decode the genom.
"""

def decode_mammoth_genome(n, s):
    if n % 4 != 0:
        return '==='
    
    t = n // 4
    count = [0] * 5
    
    for char in s:
        if char == '?':
            count[0] += 1
        elif char == 'A':
            count[1] += 1
        elif char == 'C':
            count[2] += 1
        elif char == 'G':
            count[3] += 1
        elif char == 'T':
            count[4] += 1
    
    for i in range(1, 5):
        if count[i] > t:
            return '==='
    
    result = ''
    for char in s:
        if char == '?':
            for i in range(1, 5):
                if count[i] < t:
                    count[i] += 1
                    if i == 1:
                        result += 'A'
                    elif i == 2:
                        result += 'C'
                    elif i == 3:
                        result += 'G'
                    elif i == 4:
                        result += 'T'
                    break
        else:
            result += char
    
    return result