"""
QUESTION:
Mishra has gone bizarre these days. And therefore loves only bizzare patterns. Nowadays he has ran into a habit of not listening to many "yes" or "no" from people like Bansal. In fact he does not like strings having more than one "yes" or one "no" consecutively. Bansal sends him a string of length L containing only 'Y' or 'N' for "yes" or "no" respectively. Mishra has designed a technique to convert the string into string of his liking. He picks up any two same consecutive characters and turns them into any of "YY", "YN", "NY" or "NN". Each such conversion costs Mishra one unit of energy. Help Mishra to find the conversion which costs least amount of energy or output -1 if Mishra could not perform the conversion.

Input :
            First line contains a integer T, denoting the number of test cases.
            Each test case consists of two lines.
            First line of each test case contains a single integer L representing the length of string sent by Bansal.
            Second line of each test case contains a string of L characters, each character being either 'Y' or 'N'.

Output :
            For each test case output a single integer representing the minimum energy required for conversion or output -1 if the conversion is not possible.

Constraints :
            1 ≤ T ≤ 100
            1 ≤ L ≤ 10000SAMPLE INPUT
3
2
YY
2
YN
5
YYNNY

SAMPLE OUTPUT
1
0
2
"""

def calculate_minimum_energy(test_cases):
    results = []
    map = {'N': 'Y', 'Y': 'N'}
    
    for L, string in test_cases:
        count1 = 0
        count2 = 0
        char1 = 'Y'
        char2 = 'N'
        
        for j in range(L):
            if string[j] == char1:
                count1 += 1
                char1 = map[char1]
            else:
                char1 = string[j]
            
            if string[j] == char2:
                count2 += 1
                char2 = map[char2]
            else:
                char2 = string[j]
        
        if count1 < count2:
            results.append(count1)
        else:
            results.append(count2)
    
    return results