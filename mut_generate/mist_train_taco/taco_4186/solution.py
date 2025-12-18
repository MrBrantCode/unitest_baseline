"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 

Run has given you a list of statements of the form "A+B=C", where A, B and C consist only of decimal digits and small latin letters from 'a' to 'f'. Moreover, the first symbol of A, B, C is always not a zero and the length of A, B, C is not greater than 8.  How many statements have an integer Q in the range [2; 16] such that A+B equals to C in the base Q?

------ Input ------ 

The first line of input consists of an integer T - the number of statements. Then, T statements in the form "A+B=C" (without any spaces) follow, each on a separate line.

------ Output ------ 

Output an answer to the problem of the first line of output.

------ Scoring ------ 

T = 10^{5}, Every statement is either true in the base 10, either false in all the bases : 50 points.
T = 10^{5}, No additional constraints : 50 points. 

----- Sample Input 1 ------ 
3
2+2=10
1+2=a
3+5=8
----- Sample Output 1 ------ 
2
"""

def count_valid_statements(statements):
    """
    Counts the number of statements in the form "A+B=C" that are true in any base Q in the range [2, 16].

    Parameters:
    statements (list of str): A list of strings where each string is in the form "A+B=C".

    Returns:
    int: The count of statements that are true in any base Q in the range [2, 16].
    """
    ans = 0
    for statement in statements:
        try:
            (a, bc) = statement.strip().split('+')
            (b, c) = bc.split('=')
            for base in range(16, 1, -1):
                if int(a, base) + int(b, base) == int(c, base):
                    ans += 1
                    break
        except:
            pass
    return ans