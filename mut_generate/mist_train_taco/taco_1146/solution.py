"""
QUESTION:
Today in the scientific lyceum of the Kingdom of Kremland, there was a biology lesson. The topic of the lesson was the genomes. Let's call the genome the string "ACTG".

Maxim was very boring to sit in class, so the teacher came up with a task for him: on a given string $s$ consisting of uppercase letters and length of at least $4$, you need to find the minimum number of operations that you need to apply, so that the genome appears in it as a substring. For one operation, you can replace any letter in the string $s$ with the next or previous in the alphabet. For example, for the letter "D" the previous one will be "C", and the next — "E". In this problem, we assume that for the letter "A", the previous one will be the letter "Z", and the next one will be "B", and for the letter "Z", the previous one is the letter "Y", and the next one is the letter "A".

Help Maxim solve the problem that the teacher gave him.

A string $a$ is a substring of a string $b$ if $a$ can be obtained from $b$ by deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.


-----Input-----

The first line contains a single integer $n$ ($4 \leq n \leq 50$) — the length of the string $s$.

The second line contains the string $s$, consisting of exactly $n$ uppercase letters of the Latin alphabet.


-----Output-----

Output the minimum number of operations that need to be applied to the string $s$ so that the genome appears as a substring in it.


-----Examples-----
Input
4
ZCTH

Output
2
Input
5
ZDATG

Output
5
Input
6
AFBAKC

Output
16


-----Note-----

In the first example, you should replace the letter "Z" with "A" for one operation, the letter "H" — with the letter "G" for one operation. You will get the string "ACTG", in which the genome is present as a substring.

In the second example, we replace the letter "A" with "C" for two operations, the letter "D" — with the letter "A" for three operations. You will get the string "ZACTG", in which there is a genome.
"""

def min_operations_to_genome(s: str, n: int = None) -> int:
    if n is None:
        n = len(s)
    
    if n < 4:
        raise ValueError("The length of the string must be at least 4.")
    
    genome = 'ACTG'
    min_operations = 10 ** 4  # A large initial value
    
    for i in range(n - 3):
        substring = s[i:i + 4]
        operations = 0
        for j in range(4):
            diff = abs(ord(substring[j]) - ord(genome[j]))
            operations += min(diff, 26 - diff)
        min_operations = min(min_operations, operations)
    
    return min_operations