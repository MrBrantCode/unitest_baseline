"""
QUESTION:
Recently Oz has found a magical string consisting of single digit "1". After experimenting on the string, Oz found a weird magical property of the string that is  whenever he touches the string then each digit "1" of string changed to digit "0" and each digit "0" of string changed to "01". Oz found this property interesting and immediately asked a question to RK : "How many 1's and 0's will be in the magical string if he touches the string M times ?"

Input :

The first line contains the number of test cases T . Each test case consists of a positive integer - M . 

Output :

For each test case output two space-separated integers, number of 1's and number of 0's in the magical string if Oz touches the string M times.

Constraints :

1 ≤ T ≤20

1 ≤ M ≤90

SAMPLE INPUT
2
1
2

SAMPLE OUTPUT
0 1
1 1
"""

def calculate_magical_string_counts(M):
    # Initialize the list with the initial counts after 0 touches
    l = [[1, 0]]
    
    # Compute the counts for each touch up to M if not already computed
    if M >= len(l):
        for j in range(len(l), M + 1):
            zero = l[len(l) - 1][0] + l[len(l) - 1][1]
            one = l[len(l) - 1][1]
            l.append([one, zero])
    
    # Return the counts for the M-th touch
    return tuple(l[M])