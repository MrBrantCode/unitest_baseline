"""
QUESTION:
Grey Worm has learnt that Daario Naharis's Second Sons have combined with his Unsullied to improve Daenerys's strength. The combined army is standing in a big line. You are given information of their arrangement by a string s. The string s consists of only letters 'U' and 'S', where 'U' represents an Unsullied and 'S' represents a Second Son.

Grey Worm wants inter-troop interaction among his army to be maximum. So he does not like seeing two or more Unsullied/Second Sons standing nearby (i.e. continuous) in the line. e.g. he does not like the arrangements UUS and USS, but he likes US, SUS etc.
Now by seeing the initial arrangement s of the combined army, Grey Worm may get furious and now he wants to change this arrangement into a likable arrangement. For achieving that, he can swap positions of any two Troops (not necessary continuous). Let the cost of swapping people from position i with position j (i ≠ j) be 1.

Please help Grey Worm in finding minimum cost of swaps needed to convert the current arrangement into a likable one.

Input

The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow.
Then the next line contains string s of length n, denoting the initial arrangement s of Army.
Note that the integer n is not given explicitly in input.

Output

For each test case, print a single line containing the answer of the test case, that is, the minimum cost to convert the current arrangement into a likable one. If it is not possible to convert the current arrangement into a likable one, then print -1 instead of the minimum cost.

Constraints

1 ≤ T ≤ 10^3

1 ≤ n ≤ 10^4
Register for IndiaHacksSAMPLE INPUT
8
UU
US
UUSS
USS
SUUS
UUUSS
SSUU
SUS

SAMPLE OUTPUT
-1
0
1
1
1
1
1
0

Register for IndiaHacks
"""

def minimum_swap_cost(s: str) -> int:
    countOfU = s.count('U')
    countOfS = s.count('S')
    
    # Check if it's possible to create a likable arrangement
    if countOfS > countOfU + 1 or countOfU > countOfS + 1:
        return -1
    
    # Generate the two possible likable arrangements
    firstStringToCompare = ""
    secondStringToCompare = ""
    
    for i in range(len(s)):
        if i % 2 == 0:
            firstStringToCompare += "S"
            secondStringToCompare += "U"
        else:
            firstStringToCompare += "U"
            secondStringToCompare += "S"
    
    # Calculate the differences for both possible arrangements
    StoUDiff1 = 0
    UtoSDiff1 = 0
    StoUDiff2 = 0
    UtoSDiff2 = 0
    
    for i in range(len(s)):
        if s[i] == 'S' and firstStringToCompare[i] == 'U':
            StoUDiff1 += 1
        elif s[i] == 'U' and firstStringToCompare[i] == 'S':
            UtoSDiff1 += 1
        
        if s[i] == 'S' and secondStringToCompare[i] == 'U':
            StoUDiff2 += 1
        elif s[i] == 'U' and secondStringToCompare[i] == 'S':
            UtoSDiff2 += 1
    
    # Determine the minimum swaps required
    if StoUDiff1 != UtoSDiff1 and StoUDiff2 != UtoSDiff2:
        return -1
    
    if StoUDiff1 == UtoSDiff1 and StoUDiff2 != UtoSDiff2:
        return StoUDiff1
    
    if StoUDiff2 == UtoSDiff2 and StoUDiff1 != UtoSDiff1:
        return StoUDiff2
    
    if StoUDiff2 == UtoSDiff2 and StoUDiff1 == UtoSDiff1:
        return min(StoUDiff2, StoUDiff1)