"""
QUESTION:
Ahmed Gafer failed to pass the test, but he got the job because of his friendship with Said and Shahhoud. After working in the kitchen for a while, he blew it. The customers didn't like the food anymore and one day he even burned the kitchen. Now the master Chef is very upset.
Ahmed isn't useful anymore at being a co-Chef, so S&S decided to give him a last chance. They decided to give Ahmed a new job, and make him work as the cashier of the restaurant. Nevertheless, in order not to repeat their previous mistake, they decided to give him a little test to check if his counting skills are good enough for the job. The problem is as follows: 
Given a string A of lowercase English letters, Ahmad was asked to find the number of good substrings.
A substring A[L, R] is good if:

-  The length of the substring is exactly 2 and AL = AR, OR
- The length of the substring is greater than 2,AL = AR and the substring A[L + 1, R - 1] has only one distinct letter.

Anyways, Ahmed struggled trying to find a solution for the problem. Since his mathematical skills are very poor as it turned out, he decided to cheat and contacted you asking for your help. Can you help him in this challenge?

-----Input-----
The first line of the input contains the integer T, indicating the number of test cases.
Each of the following T lines, contains a string A.

-----Output-----
For each test case, output a single line containing a single number, indicating the number of good substrings.

-----Constraints-----

- 1 ≤ T ≤ 100 
- 1 ≤  |A|  ≤ 105 
-  It's guaranteed that the sum of  |A|  over all test cases doesn't exceed 5x105. 

-----Example-----
Input:
2
a
abba

Output:
0
2


-----Explanation-----
Example case 2. The good substrings of abba are: { bb } and { abba }.
"""

def count_good_substrings(A: str) -> int:
    n = len(A)
    ans = 0
    temp = []
    l = 0
    count = 1
    current = A[0]
    start = 0
    end = 0
    i = 1
    
    while i < n:
        if A[i] == current:
            count += 1
            end += 1
        else:
            if count > 0:
                temp.append([start, end])
                l += 1
            count = 1
            current = A[i]
            start = i
            end = i
        i += 1
    
    if count > 0:
        temp.append([start, end])
        l += 1
    
    for i in range(l):
        le = temp[i][1] - temp[i][0] + 1
        if le >= 2:
            val = le * (le - 1) // 2
            ans += val
        x = temp[i][0] - 1
        y = temp[i][1] + 1
        if x >= 0 and y < n and (A[x] == A[y]):
            ans += 1
    
    return ans