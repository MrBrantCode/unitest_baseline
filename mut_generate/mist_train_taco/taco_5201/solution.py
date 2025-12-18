"""
QUESTION:
Manasa recently lost a bet to Amit. To settle the problem, they are playing a game:  

They have N balls in front of them. Each ball, except the 1st ball, is numbered from 0 to 9. The 1st ball is numbered from 1 to 9. 

Amit calculates all the subsequences of the number thus formed. Each subsequence of sequence S is represented by S_{k}. 

e.g. S = 1 2 3  

S_{0} = 1 2 3 , 

S_{1} = 1 2 , 

S_{2} = 1 3 , 

S_{3} = 2 3 , 

S_{4} = 1 , 

S_{5} = 2 , and 

S_{6} = 3 .  

Each subsequence S_{k} also represents a number. e.g. S_{1} represents tweleve, S_{2} represents thirteen.

Now Manasa has to throw S_{k} candies into an intially empty box, where k goes from 0 to ( maximum number of subsequences -  1).

At the end of the game, Manasa has to find out the total number of candies, T, in the box. As T can be large, Amit asks Manasa to tell T % (10^{9} + 7 ). If Manasa answers correctly, she can keep all the candies. Manasa can't take all this Math and asks for your help.  

Help her!

Note: A subsequence can also be have preceding zeros. For example, the sequence 103 has subsequences 103, 10, 13, 03, 1, 0, and 3 (so both 03 and 3 are counted separately).

Input Format 

A single line containing a number having N digits.  

Output Format 

A number contaning the output.  

Constraints 

1 ≤ N ≤ 2*10^{5}  

Sample Input 00

111

Sample Output 00

147

Sample Input 01

123

Sample Output 01

177

Explanation  

The subsequence of number 111 are 111, 11 , 11, 11, 1, 1 and 1. Whose sum is 147.

The subsequence of number 123 are 123, 12 , 23, 13, 1, 2 and 3. Whose sum is 177.
"""

def calculate_total_candies(number_str: str) -> int:
    P = 10**9 + 7
    s = [ord(c) - ord('0') for c in number_str]
    ret = 0
    for i, x in enumerate(s):
        ret = (11 * ret + x * pow(2, i, P)) % P
    return ret