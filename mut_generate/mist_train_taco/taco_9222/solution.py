"""
QUESTION:
Again a simple task from Oz! He has given you two strings STR1 and STR2. Each character of both strings is from the set {A, B, C, D, E, F, G, H, I, J}. You can perform 3 types of conversions on string STR1 :
Replace a character(except 'J') by next character from the set.
   i.e "ABE" to "ACE" 
Replace a character(except 'A') by previous  character from the
   set. i.e "ABE" to "ABD" 
Swap any two    characters. i.e "ABE" to "EBA"

Now you have to convert STR1 into STR2 using minimum number of conversions. Output the minimum number of conversions required.

Input:
First line of the input contains a single integer T  denoting the number of test cases.
Each test case consist of two lines. First line contains STR1 and second line contains STR2.

Output:
For each test case, output minimum number of conversions required.

Constraints:
1 ≤ T ≤ 10
1 ≤ |STR1| ≤ 8
|STR1| = |STR2|

SAMPLE INPUT
1
BC
DA

SAMPLE OUTPUT
3

Explanation

Following are 3 conversion steps :
- first swap 'B' and 'C' so STR1 becomes "CB"
- Replace 'C' by next character 'D' so STR1 becomes "DB"
- Replace 'B' by previous character 'A' so STR1 becomes "DA"
we can not convert STR1 into STR2 in fewer than 3 steps.
"""

def minimum_conversions(str1, str2):
    def minoper(str1, str2):
        l = len(str1)
        if l == 1:
            return abs(ord(str1[0]) - ord(str2[0]))
        minnum = float('inf')
        minnum = min(minnum, minoper(str1[1:], str2[1:]) + abs(ord(str1[0]) - ord(str2[0])))
        for i in range(1, l):
            str11 = list(str1)
            str22 = list(str2)
            str22[0], str22[i] = str22[i], str22[0]
            minnum = min(minnum, 1 + minoper(str11[1:], str22[1:]) + abs(ord(str11[0]) - ord(str22[0])))
        return minnum
    
    return minoper(list(str1), list(str2))