"""
QUESTION:
You are given a string S consisting of digits between 1 and 9, inclusive.
You can insert the letter + into some of the positions (possibly none) between two letters in this string.
Here, + must not occur consecutively after insertion.
All strings that can be obtained in this way can be evaluated as formulas.
Evaluate all possible formulas, and print the sum of the results.

-----Constraints-----
 - 1 \leq |S| \leq 10
 - All letters in S are digits between 1 and 9, inclusive.

-----Input-----
The input is given from Standard Input in the following format:
S

-----Output-----
Print the sum of the evaluated value over all possible formulas.

-----Sample Input-----
125

-----Sample Output-----
176

There are 4 formulas that can be obtained: 125, 1+25, 12+5 and 1+2+5. When each formula is evaluated,
 - 125
 - 1+25=26
 - 12+5=17
 - 1+2+5=8
Thus, the sum is 125+26+17+8=176.
"""

def sum_of_formulas(S: str) -> int:
    total = 0
    length = len(S)
    
    # Generate all possible formulas by inserting '+'
    for i in range(length):
        for j in range(length - i):
            n = int(S[j:j + i + 1])
            if j == 0 or j == length - i - 1:
                total += n * max([2 ** (length - i - 2), 1])
            else:
                total += n * max([2 ** (length - i - 3), 1])
    
    return total