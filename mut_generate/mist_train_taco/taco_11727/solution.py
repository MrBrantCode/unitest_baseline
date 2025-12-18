"""
QUESTION:
You will be given m strings. For each of those strings, you need to count the total number of appearances of that string as substrings in all possible strings of length n containing only lower case English letters. 

A string may appear in a string multiple times. Also, these appearances may overlap. All these must be counted separately. For example, aa appears thrice in the string aaacaa: aaacaa, aaacaa and aaacaa.

-----Input-----
- The first line contains one integer, T, the number of test cases. The description of each test case follows:
- The first line of each test case will contain two integers n and m.
- The ith of the next m lines will have one string in each line. All the strings will consist only of lower case English letters.

-----Output-----
- For each test case, print "Case x:" (without quotes. x is the test case number, 1-indexed) in the first line.
- Then print m lines. The ith line should contain the number of appearances of the ith string in all possible strings of length n. As the numbers can be very large, print the answers modulo 109+7.

-----Constraints-----
- 1 ≤ T ≤ 100
- 1 ≤ n ≤ 100000
- 1 ≤ m ≤ 1000 
- 1 ≤ Length of every string in input
- 1 ≤ Total length of all strings in one test case ≤ 5 * 105
- 1 ≤ Total length of all strings in one test file ≤ 5 * 106

-----Example-----
Input:
3
2 1
aa
2 1
d
12 3
cdmn
qweewef
qs

Output:
Case 1:
1
Case 2:
52
Case 3:
443568031
71288256
41317270

-----Explanation:-----
Testcase 1: aa is the only string of length 2 which contains aa as a substring. And it occurs only once. Hence the answer is 1.
"""

def count_substring_appearances(test_cases):
    MOD = 1000000007
    results = []
    
    for idx, case in enumerate(test_cases, start=1):
        n = case['n']
        m = case['m']
        strings = case['strings']
        
        case_result = {
            'case_number': idx,
            'counts': []
        }
        
        for s in strings:
            ls = len(s)
            if ls > n:
                case_result['counts'].append(0)
            else:
                k = n - ls + 1
                count = k * pow(26, n - ls, MOD) % MOD
                case_result['counts'].append(count)
        
        results.append(case_result)
    
    return results