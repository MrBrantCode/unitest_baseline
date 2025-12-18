"""
QUESTION:
Read problems statements in Mandarin chinese, Russian and Vietnamese as well. 

Given an integer A that contains n > 1 digits. You are asked to remove exactly one digit to make the result number is divisible by 6, also make it biggest possible.
 
------ Input ------ 

The first line contains an integer T, denotes the number of test cases. Each test case is described by an integer A in a single line.
 
------ Output ------ 

Each test case, output the answer on a single line (it's allowed to delete a digit such that the resulting number contains leading zeroes, you shouldn't remove them in this case). If it is impossible to make the result number satisfies the above condition,
output -1.
 
------ Constraints ------ 

$1 ≤ T ≤ 100$
$2 ≤ n ≤ 10^{5}$
$A will not contain leading zeroes$
$the sum of n over all test cases ≤ 10^{6}$

Subtasks:

$Subtask #1 (30 points): the sum of n over all test cases ≤ 2000$
$Subtask #2 (70 points): original constrains$

----- Sample Input 1 ------ 
3
123
100222
10003
----- Sample Output 1 ------ 
12
00222
-1
"""

def find_largest_divisible_by_6(A: str) -> str:
    a = [int(c) for c in A]
    asu = sum(a)
    amod = asu % 3
    
    if a[-1] % 2 != 0:
        if a[-2] % 2 == 0:
            adiv3 = amod - a[-1]
            if adiv3 == 0 or adiv3 == -3 or adiv3 == -6 or adiv3 == -9:
                return A[:-1]
            else:
                return "-1"
        else:
            return "-1"
    else:
        max1 = -1
        for i in range(1, len(a) - 1):
            adiv3 = amod - a[i]
            if adiv3 == 0 or adiv3 == -3 or adiv3 == -6 or adiv3 == -9:
                max1 = i
                if a[i + 1] > a[i]:
                    break
        
        adiv3 = amod - a[-1]
        if a[-2] % 2 == 0:
            if adiv3 == 0 or adiv3 == -3 or adiv3 == -6 or adiv3 == -9:
                if max1 == -1 or a[max1] > a[max1 + 1]:
                    max1 = len(a) - 1
        
        adiv3 = amod - a[0]
        if adiv3 == 0 or adiv3 == -3 or adiv3 == -6 or adiv3 == -9:
            if max1 == -1 or a[1] > a[0]:
                max1 = 0
        
        if max1 == -1:
            return "-1"
        else:
            return A[0:max1] + A[max1 + 1:]